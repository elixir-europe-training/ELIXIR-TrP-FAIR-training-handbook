cp checklist_head.md checklist.md
Rscript create_md_checklist.R --input ../docs/assets/checklist_large.xlsx >> checklist.md
mv checklist.md ../docs
