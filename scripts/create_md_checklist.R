#! /usr/bin/env Rscript

# Load libraries
library(readxl)
library(dplyr)
library(optparse)
library(knitr)
library(kableExtra)

option_list <- list(
    make_option(c("-i", "--input"),
        type = "character",
        help = "Excel table with checklist"
    )
)

opt_parser <- OptionParser(
    option_list = option_list,
    description = "Generates markdown table from excel table with checklist"
)
opt <- parse_args(opt_parser)

# Read in data
md_checklist <- read_excel(opt$input,
    sheet = "for_review"
)

md_checklist <- select(
    md_checklist, "TFC INDICATOR", "TFC TERM", "TFC PRIORITY",
    "Bioschema Property (click on cell to be taken to property information)",
    "Bioschema marginality", "RDA_PRINCIPLE", "RDA INDICATOR_ID"
)

colnames(md_checklist) <- c(
    "indicator",
    "term", "priority",
    "bioschemas_property", "bioschemas_marginality", "rda_principle",
    "rda_indicator_id"
)

md_table <- knitr::kable(md_checklist,  format = "markdown")

write(md_table, stdout())
