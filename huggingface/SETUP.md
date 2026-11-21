# Weekly email dataset sync

Destination: https://huggingface.co/datasets/GarethFW/Accessible_Email_Design

1. Open [Actions variables](https://github.com/Double-FW/Accessible-Email-Design/settings/variables/actions). Add or edit the ordinary variable `HF_DATASET_ID` to `GarethFW/Accessible_Email_Design`. This is a dataset name, not the token or a full URL.
2. Open https://huggingface.co/settings/tokens and create a Fine-grained/Custom token. Under repository permissions select only `GarethFW/Accessible_Email_Design` and grant read and write access. Leave unrelated permissions unticked. Copy the generated token beginning `hf_` privately.
3. Open [Actions secrets](https://github.com/Double-FW/Accessible-Email-Design/settings/secrets/actions). Add or update `HF_TOKEN` with that generated token, using an underscore. Do not paste the dataset name into the token field or share the token in chat.
4. Open [the workflow](https://github.com/Double-FW/Accessible-Email-Design/actions/workflows/huggingface-sync.yml), choose Run workflow on main, and inspect the new run. Confirm successful publication and the destination Files tab before reporting the sync complete.

Schedule: Monday 10:19 UTC (10:19 UK winter, 11:19 UK summer). GitHub may delay scheduled runs or disable schedules in inactive public repositories. Manual Run workflow is available.

The source must remain public and the existing destination must be initialised. GitHub’s automatically supplied read-only token authenticates the public-source check; no additional GitHub token is needed. HF_TOKEN is supplied only to the publishing step. Only eight managed output files are committed atomically against the destination revision. Unrelated files, including `.gitattributes`, and destination visibility are preserved. A no-change run creates no dataset commit.

The export contains seven complete guidance documents, 16 learning sections as an alternative view of the guide, and eight activities with 16 illustrative prompts. Full source text, shared scope, authority, local design qualifications, original dates and rights context are preserved. These are source material and instructional examples, not completed client tests, recipient outcomes or independently validated answers. Linked external source bodies are not copied. No test/audit report is published in source or dataset; diagnostics stay in the workflow log. Provenance and schema describe source origin and format only.

The allowlist is explicit. New files, changed licences or a changed destination require review before changing configuration. Missing/dirty approved source, invalid structure, a wrong dataset or a token field containing the dataset name stops publication. Do not confuse these checks with an email-client, delivery, legal or model evaluation.

For local checks, install `huggingface/requirements.txt`, then run `python scripts/export_huggingface.py --check-only` and `python -m unittest discover -s tests -v`. Build with `python scripts/export_huggingface.py --output /tmp/email-preview --dataset-id GarethFW/Accessible_Email_Design`. Regression tests use a simulated destination and no real credentials.
