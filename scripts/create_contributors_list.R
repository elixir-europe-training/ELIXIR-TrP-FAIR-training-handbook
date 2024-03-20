library(googlesheets4)
library(dplyr)

gs4_deauth()

contr_list <- read_sheet("https://docs.google.com/spreadsheets/d/1MRv1CauwmMRM2GCnFBtrfcMyF9hYHbw1slbKb_aXklI/edit#gid=1378181774",
    sheet = "contributors from all events"
)

contr_list <- rename(contr_list, github_name = "GitHub name") |>
    mutate(
        orcid_link = ifelse(ORCID == "", "", paste0(
            "[:custom-orcid:](https://orcid.org/",
            ORCID,
            "/)"
        )),
        github_link = ifelse(github_name == "", "", paste0(
            "[:simple-github:](https://github.com/",
            github_name,
            "/)"
        ))
    ) |> 
    arrange(Name)

writeLines(paste(
    "-", contr_list$Name,
    ifelse(is.na(contr_list$orcid_link), "", contr_list$orcid_link),
    ifelse(is.na(contr_list$github_link), "", contr_list$github_link)
), "docs/contributor_list.md")
