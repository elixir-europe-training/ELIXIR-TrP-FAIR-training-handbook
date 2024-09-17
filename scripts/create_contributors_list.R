

library(dplyr)
library(googledrive)
library(readxl)

drive_deauth()
drive_auth_configure()

dl <- drive_download(
  as_id(
    "https://docs.google.com/spreadsheets/d/1Nk0Fbx5PtFYxz6xB6YSzLlhHb-N6J2nb/edit?gid=1360009440"
  ),
  path = "temp1.xlsx",
  overwrite = TRUE
)

drive_api_key()

contr_list <-
  readxl::read_excel("temp1.xlsx", sheet = "contributors from all events")

file.remove('temp1.xlsx')

contr_list <- rename(contr_list, github_name = "GitHub name") |>
  mutate(
    orcid_link = ifelse(
      ORCID == "",
      "",
      paste0("[:custom-orcid:](https://orcid.org/",
             ORCID,
             "/)")
    ),
    github_link = ifelse(
      github_name == "",
      "",
      paste0("[:simple-github:](https://github.com/",
             github_name,
             "/)")
    )
  ) |>
  arrange(Name)

writeLines(paste(
  "-",
  contr_list$Name,
  ifelse(is.na(contr_list$orcid_link), "", contr_list$orcid_link),
  ifelse(is.na(contr_list$github_link), "", contr_list$github_link)
),
"docs/contributor_list.md")
