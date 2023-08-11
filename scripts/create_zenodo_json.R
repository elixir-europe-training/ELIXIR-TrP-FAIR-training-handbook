library(googlesheets4)
library(dplyr)
library(jsonlite)

contr_list <- read_sheet("https://docs.google.com/spreadsheets/d/1MRv1CauwmMRM2GCnFBtrfcMyF9hYHbw1slbKb_aXklI/edit#gid=1378181774",
    sheet = "contributors from all events"
)

# rename columns according to zenodo schema
contr_list <- rename(contr_list,
    name = "Name",
    affiliation = "Affiliation",
    orcid = "ORCID",
    github = "GitHub name"
)

# create zenodo json object
zenodo_json <- toJSON(
    list(
        upload_type = "lesson",
        title = "ELIXIR fair training handbook",
        license = "cc-by-sa-4.0",
        creators = contr_list[, c(
            "name",
            "affiliation",
            "orcid",
            "github"
        )]
    ),
    pretty = TRUE
)

write(zenodo_json, ".zenodo.json")
