"""Committed-source and fixed-destination rules for email publication."""
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import urllib.request
import urllib.error

ROOT=Path(__file__).resolve().parents[1]
SOURCE='Double-FW/Accessible-Email-Design'
TARGET='GarethFW/Accessible_Email_Design'
MANAGED=('README.md','LICENSE','NOTICE.md','documents.jsonl','learning_sections.jsonl','activities.jsonl','provenance.json','record_schema.json')
CONFIG='huggingface/export-config.json'

def digest(data):return hashlib.sha256(data).hexdigest()
def git(root,*args):return subprocess.check_output(['git','-C',str(root),*args])
def destination(value):
    if value!=TARGET:raise ValueError('HF_DATASET_ID must be '+TARGET+'.')
    return value

def committed(root,path):
    p=PurePosixPath(path)
    if p.is_absolute() or '..' in p.parts or any(x.startswith('.') for x in p.parts):raise ValueError('Invalid approved source path: '+path)
    info=git(root,'ls-tree','HEAD','--',path).decode().strip()
    if not info.startswith('100644 blob '):raise ValueError('Required source must be a committed regular file: '+path)
    sha=info.split()[2];data=git(root,'cat-file','blob',sha)
    if hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()!=sha:raise ValueError('Git source integrity failed: '+path)
    return data,{'path':path,'git_blob_sha':sha,'sha256':digest(data),'size_bytes':len(data)}

def read_sources(root=ROOT):
    raw,entry=committed(root,CONFIG);cfg=json.loads(raw)
    if cfg['source_repository']!=SOURCE:raise ValueError('Wrong source repository in export configuration.')
    destination(cfg['destination_dataset'])
    paths=cfg['source_files']
    if not isinstance(paths,list) or len(paths)!=len(set(paths)) or not all(isinstance(p,str) for p in paths):raise ValueError('Source allowlist must contain unique paths.')
    required={'README.md','AGENTS.md','LICENSE','NOTICE.md','Email_Accessibility.md','Terminology_Alignment.md','Related_Double_FW_Guidance.md','Production_Workflow_and_Handoff_Map.md','Accessible-Email-Design-RAG-and-Prompts/Content_Creation_and_Production_Activities_and_Prompts.md'}
    if not required<=set(paths):raise ValueError('Required guidance, authority and activity sources must remain included.')
    texts={};manifest=[entry]
    for path in paths:
        data,e=committed(root,path);text=data.decode('utf-8')
        if any(x in text for x in ['chatgpt.com/library?','account_id=personal','file_id=libfile_']):raise ValueError('Personal source-access locator in public export: '+path)
        texts[path]=text;manifest.append(e)
        working=Path(root)/path
        if not working.is_file() or working.is_symlink() or working.read_bytes()!=data:raise ValueError('Working source differs from the committed snapshot: '+path)
    if digest(texts['LICENSE'].encode())!=cfg['approved_license_sha256']:raise ValueError('Licence bytes changed; review before publication.')
    return cfg,texts,manifest

def public_source():
    headers={'User-Agent':'Double-FW-email-dataset-sync','Accept':'application/vnd.github+json'}
    token=os.environ.get('GITHUB_TOKEN')
    if token:headers['Authorization']='Bearer '+token
    request=urllib.request.Request('https://api.github.com/repos/'+SOURCE,headers=headers)
    try:
        with urllib.request.urlopen(request,timeout=30) as response:info=json.load(response)
    except urllib.error.HTTPError as e:
        raise ValueError('Public GitHub source verification failed (HTTP '+str(e.code)+'). Check the workflow GitHub token and API availability; no Hugging Face write was attempted.') from None
    except urllib.error.URLError:
        raise ValueError('Public GitHub source verification could not reach the API; no Hugging Face write was attempted.') from None
    if info.get('full_name')!=SOURCE or info.get('private') is not False or info.get('visibility')!='public':raise ValueError('Publishing requires the approved public GitHub source.')
