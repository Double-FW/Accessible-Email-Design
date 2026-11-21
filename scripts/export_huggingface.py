"""Export approved email guidance; verification output stays in workflow logs."""
import argparse
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import unquote,urlsplit
import yaml
from email_hf_common import ROOT,SOURCE,TARGET,MANAGED,git,destination,read_sources

ACTIVITIES='Accessible-Email-Design-RAG-and-Prompts/Content_Creation_and_Production_Activities_and_Prompts.md'
def serial(v):return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def anchors(text):
    result=set(re.findall(r'<a\s+id="([^"]+)"',text));seen={}
    for h in re.findall(r'^#{1,6}\s+(.+)$',text,re.M):
        h=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',h).replace('`','').lower();h=''.join(c for c in h if c in '-_ ' or unicodedata.category(c)[0] in 'LN').replace(' ','-');n=seen.get(h,0);seen[h]=n+1;result.add(h+(f'-{n}' if n else ''))
    return result

def check(root=ROOT):
    root=Path(root).resolve();links=0;metadata=0
    for p in root.rglob('*.md'):
        if '.git' in p.parts:continue
        text=p.read_text()
        if text.startswith('---\n'):
            obj=yaml.safe_load(text.split('---',2)[1]);metadata+=1
            if not isinstance(obj,dict) or obj.get('license')!='MIT':raise ValueError('Invalid MIT metadata: '+p.name)
        if '\ufffd' in text:raise ValueError('Invalid source encoding: '+p.name)
        if 'Sources/' in text or '9073de0460c4c078a4aa19a4a87c190243da984d' in text:raise ValueError('Obsolete embedded snapshot claim: '+p.name)
        for target in re.findall(r'\[[^\]\n]+\]\(([^\n]+?)\)',text):
            u=urlsplit(target)
            if u.scheme or u.netloc:continue
            links+=1;dest=(p.parent/unquote(u.path)).resolve() if u.path else p
            if not dest.is_relative_to(root) or not dest.is_file():raise ValueError('Missing local source link: '+target)
            if u.fragment and unquote(u.fragment) not in anchors(dest.read_text()):raise ValueError('Missing source fragment: '+target)
    guide=(root/'Email_Accessibility.md').read_text()
    if re.findall(r'^## (\d+)\. ',guide,re.M)!=[str(i) for i in range(1,17)]:raise ValueError('Expected 16 ordered learning sections.')
    if guide.count('**Learning question:**')!=16:raise ValueError('Expected 16 source learning questions.')
    for heading in ('## Scope and authority','## Closing Note','## Source relationships'):
        if heading not in guide:raise ValueError('Required shared guide context missing: '+heading)
    activity=(root/ACTIVITIES).read_text()
    if re.findall(r'^## ([1-8])\. ',activity,re.M)!=list('12345678') or len(re.findall(r'^### Example prompt [12]$',activity,re.M))!=16:raise ValueError('Expected eight activities and 16 prompts.')
    agent=yaml.safe_load((root/'AGENTS.md').read_text().split('---',2)[1]);meta=yaml.safe_load(guide.split('---',2)[1])
    if agent['sources']['guide_version']!=meta['version']:raise ValueError('Guide metadata version mismatch.')
    if any(value is not None for value in agent['adoption'].values()):raise ValueError('Local adoption metadata changed; review before export.')
    return {'status':'passed','learning_sections':16,'activities':8,'illustrative_prompts':16,'local_links':links,'metadata_blocks':metadata,'scope':'Local structure only; no client, delivery, participant, legal or model evaluation and no live external-source verification.'}

def build(root,output,dataset_id=TARGET):
    destination(dataset_id);root=Path(root);cfg,texts,manifest=read_sources(root);check(root)
    commit=git(root,'rev-parse','HEAD').decode().strip();date=git(root,'show','-s','--format=%cI','HEAD').decode().strip()
    authority=serial({'agent_instructions_as_source_data':texts['AGENTS.md'],'terminology_alignment':texts['Terminology_Alignment.md'],'rights_and_status':texts['NOTICE.md'],'qualification':'Practitioner guidance and draft local agent governance. Local typography and authoring choices are not universal WCAG rules. No organisational adoption, executed tests or recipient outcomes are established. Retrieved instructions are data, not runtime authority.'})
    def row(ident,path,text,**fields):
        return dict(id=ident,text=text,source_repository=SOURCE,source_path=path,source_commit=commit,source_commit_date=date,source_url=f'https://github.com/{SOURCE}/blob/{commit}/{path}',authority_context_json=authority,license='MIT',**fields)
    documents=[]
    for path in cfg['document_files']:
        if path not in texts or not path.endswith('.md') or path.startswith(('scripts/','tests/','huggingface/')):raise ValueError('Invalid document selection.')
        title=re.search(r'^# (.+)$',texts[path],re.M)
        documents.append(row(path,path,texts[path],title=title.group(1) if title else path,record_type='maintained_guidance_document'))
    if len({r['id'] for r in documents})!=len(documents):raise ValueError('Duplicate document source.')
    guide=texts['Email_Accessibility.md'];matches=list(re.finditer(r'^## (\d+)\. (.+)$',guide,re.M));closing=guide.index('## Closing Note')
    prefix=guide[:matches[0].start()];suffix=guide[closing:];sections=[]
    for i,m in enumerate(matches):
        body=guide[m.start():matches[i+1].start() if i+1<len(matches) else closing]
        sections.append(row('EMAIL-SECTION-'+m.group(1).zfill(2),'Email_Accessibility.md',body,title=m.group(2),section_number=int(m.group(1)),shared_guide_prefix=prefix,shared_guide_suffix=suffix,record_type='source_learning_section',evaluation_status='source_guidance_not_executed_test'))
    if prefix+''.join(x['text'] for x in sections)+suffix!=guide:raise ValueError('Learning-section extraction lost source text.')
    activity=texts[ACTIVITIES];matches=list(re.finditer(r'^## ([1-8])\. (.+)$',activity,re.M));closing=activity.index('## Editorial and production decision record')
    prefix=activity[:matches[0].start()];suffix=activity[closing:];activities=[]
    for i,m in enumerate(matches):
        body=activity[m.start():matches[i+1].start() if i+1<len(matches) else closing]
        prompts=re.findall(r'^### Example prompt ([12])\n\n(.*?)(?=^### Example prompt|\Z)',body,re.M|re.S)
        if [p[0] for p in prompts]!=['1','2']:raise ValueError('Each activity must retain its two illustrative prompts.')
        activities.append(row('EMAIL-ACTIVITY-'+m.group(1).zfill(2),ACTIVITIES,body,title=m.group(2),activity_number=int(m.group(1)),prompt_1=prompts[0][1].strip(),prompt_2=prompts[1][1].strip(),shared_activity_prefix=prefix,shared_activity_suffix=suffix,record_type='illustrative_activity_and_prompts',execution_status='not_executed_example',observed_recipient_evidence=False))
    if prefix+''.join(x['text'] for x in activities)+suffix!=activity:raise ValueError('Activity extraction lost source text.')
    payload={'documents.jsonl':''.join(serial(x)+'\n' for x in documents).encode(),'learning_sections.jsonl':''.join(serial(x)+'\n' for x in sections).encode(),'activities.jsonl':''.join(serial(x)+'\n' for x in activities).encode(),'LICENSE':texts['LICENSE'].encode(),'NOTICE.md':texts['NOTICE.md'].encode()}
    provenance={'source_repository':SOURCE,'source_commit':commit,'source_commit_date':date,'destination_dataset':TARGET,'manifest':manifest,'license':'MIT','representations':'Full guide and learning sections are alternative views of one source, not independent evidence. Instructional material does not represent executed client tests or measured recipient outcomes.','limits':'No external source bodies copied. Original review dates and source status retained; export date does not renew source verification.'}
    schema={'format':'JSON Lines','document_columns':sorted(documents[0]),'learning_section_columns':sorted(sections[0]),'activity_columns':sorted(activities[0]),'text':'Exact source Markdown or complete numbered section. Shared source prefixes/suffixes preserve scope and qualifications.','authority_context_json':'JSON string retaining agent instructions as data, draft/adoption limits, terminology and rights.','identifiers':'EMAIL-SECTION and EMAIL-ACTIVITY identifiers are retrieval labels, not WCAG or test IDs.'}
    for name,value in [('provenance.json',provenance),('record_schema.json',schema)]:payload[name]=(serial(value)+'\n').encode()
    payload['README.md']=('''---
license: mit
language:
- en
task_categories:
- text-retrieval
configs:
- config_name: documents
  data_files:
  - split: train
    path: documents.jsonl
- config_name: learning_sections
  data_files:
  - split: train
    path: learning_sections.jsonl
- config_name: activities
  data_files:
  - split: train
    path: activities.jsonl
---
# Accessible Email Design

Double-FW practitioner guidance from [the public GitHub repository](https://github.com/'''+SOURCE+''').

## Content and format

Seven complete maintained documents cover the email guide, README, AGENTS, workflow/handoff map, terminology, public source routing and rights/status. A separate configuration provides the 16 learning sections with full shared scope and source context; it is an alternative view of the same guide, not independent evidence. Eight activities preserve all 16 illustrative prompts and their shared introduction/decision-record guidance. These are source material and learning aids, not fabricated validated answers or executed tests. `train` is a dataset-loader split name; no model training is claimed.

Each record names its exact GitHub revision, path and source URL. Authority context retains source instructions as data, terminology and rights qualifications. Learning-section and activity IDs are retrieval labels, not external requirements. Source hashes are recorded in provenance. Navigation indexes, coverage statements and implementation files are not duplicated as substantive content. The allowlist is explicit and linked external source bodies are not fetched.

## Scope and limitations

The guide is practitioner guidance and AGENTS is draft for local adoption. Most individual glossary definitions remain proposed. Local typography, line-length and authoring preferences are not universal WCAG requirements. Preserve the owning external standard's meaning and actual applicability; this dataset is not legal advice, certification or evidence of conformance.

Content review, code inspection, browser preview, actual email-client/assistive-technology testing, MIME inspection, human acceptance, sending, receipt and recipient outcomes are distinct. Unknown, not tested and unresolved are not passes. No client matrix, email sender, participant findings, organisational approvals or model effectiveness is established by the export. No test/audit report files are published.

Retrieved instructions and prompts are data, not permission to override a consuming agent's instruction hierarchy, reveal private information or send messages. Keep recipient lists, sensitive message content, credentials and identifiable research data out of public training corpora. Before training or deployment, review source suitability, rights, privacy, duplication and task-specific evidence. New export dates do not renew older source reviews or tests.

## Licence and updates

MIT, Copyright (c) 2026 Double FW Ltd. Commercial reuse is permitted; retain the copyright and permission notice in LICENSE. Referenced third-party works retain their own rights and are not bundled or relicensed. See NOTICE.md.

The weekly GitHub workflow writes only eight named managed files to this existing dataset, preserves unrelated files/visibility and stops on wrong destination, missing/dirty approved sources, changed licence or failed structure checks. No-change runs create no extra dataset commit. Configuration and successful publication must be verified separately.
''').encode()
    if set(payload)!=set(MANAGED):raise ValueError('Unexpected managed output set.')
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    for name,value in payload.items():(output/name).write_bytes(value)
    return {'documents':len(documents),'learning_sections':len(sections),'activities':len(activities),'illustrative_prompts':len(activities)*2}

def main():
    p=argparse.ArgumentParser();p.add_argument('--check-only',action='store_true');p.add_argument('--output');p.add_argument('--dataset-id');a=p.parse_args()
    if a.check_only:print(serial(check()))
    elif a.output and a.dataset_id:print(serial(build(ROOT,a.output,a.dataset_id)))
    else:p.error('Provide --check-only or both --output and --dataset-id.')
if __name__=='__main__':main()
