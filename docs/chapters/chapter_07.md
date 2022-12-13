---
tags:
    - Metadata
    - Contextual information
    - Reusability
    - Learning outcomes
---
<!-- Chapter title: Make it reusable --> 


## Description

In this chapter, we explore the type of information required for people to decide if and how they can reuse training materials they are otherwise unfamiliar with. This information is an important part of the metadata and should be included alongside the materials. We consider existing metadata recommendations for training materials and different ways of representing this information in a detailed but logical and useful format.

In this chapter training materials can be either an individual training material (e.g. a dataset, slides) or a collection of materials associated with a particular training session.

!!! info "Learning outcomes"

    By the end of this chapter, learners will be able to:

    1. List the information which will allow other trainers to reuse training materials
    2. Write learning outcomes that clearly articulate training goals
    3. Choose a suitable method for sharing contextual information about their training materials.
    4. Construct a detailed description (run sheet/recipe) which will allow others to reuse their training materials


## Prerequisites

How you manage the metadata associated with your training materials depends on where and in what format you are sharing your materials. It’s recommended that you read [Chapter 2: Structure materials for FAIRness](https://elixir-fair-training.github.io/FAIR-training-handbook/chapters/chapter_02/) and  [Chapter 3 - getting ready reate your materials for reuse](https://elixir-fair-training.github.io/FAIR-training-handbook/chapters/chapter_03/) before starting on this chapter.


## Introduction

Imagine you have made the most delicious cake ever to be created. Perhaps it is a multi-layered chocolate cake with cream and cherries on top. Believing that food is better when shared, you want to make sure that your friends and family can make it too. How would you go about doing this?

You’d likely start with a recipe. This recipe would include a description of the cake, a list of ingredients and equipment, and instructions on how to combine the ingredients. You might also include extra information like how many people it serves or tips on steps that can be done ahead of time. 

Your friend decides to bake the cake but they can’t eat cherries and don’t have some of the ingredients and equipment that you have. They decide to experiment by substituting ingredients and methods from another recipe to make their own perfect chocolate cake. 

The same is true for training. The training session can be thought of as the cake, the training materials are the ingredients, and the methods are instructions on how to combine and use the materials to deliver the training. 

Training materials and sessions can be reused in whole, in part or simply as inspiration. Regardless, when reusing training materials it is likely that they will need to be adapted to new contexts to account, for example, for different audiences and settings. To enable others to reuse your materials it’s important to provide a detailed recipe.


## What to include in your recipe

!!! example "Learning activity: What to include in your recipe"

    In this activity we consider what types of information to include in a training recipe. 


    1. Find three examples of training materials relevant to your field. This may be an individual training material or a training session. (Alternatively, take a look at some of the case studies linked below).
    2. What information is included in the training recipe for these materials?
    3. Is the same information provided in all three examples?
    4. Would you need more information to decide whether you could reuse them and how?

Information about training sessions and materials is referred to as [metadata](https://faircookbook.elixir-europe.org/content/recipes/introduction/metadata-fair.html). Metadata makes it easier for you and others to understand how a particular material or set of materials can be reused. 

Making training FAIR requires materials and sessions to be described with rich metadata. Ideally, this includes a universally agreed set of information. Many training communities, including [Bioschemas](https://bioschemas.org/profiles/Course/0.9-DRAFT-2020_12_08) and the [Research Data Alliance (RDA)](https://www.google.com/url?q=https://doi.org/10.15497/RDA00073&sa=D&source=docs&ust=1661905403636069&usg=AOvVaw17J5RLnyWOwcoTVR6YbELT) [@hoebelheinrich_nancy_j_2022_6769695], are working towards defining these sets of information but broad agreement on the categories to be included is yet to be reached. In our paper [10 simple rules for making training materials FAIR](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007854) [@Garcia2020] we used the Bioschema and RDA sets to create a list of the information (metadata) that is important for training materials.

**Table 1:** Metadata that is important for training materials and guidance on what to include in each category (reproduced from Garcia _et al_ 2020 [@Garcia2020] under CC BY 4.0)

| **Type of metadata**      | **What to include**                                                                                                                                       |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Title                      | Title of the training material.                                                                                                                            |
| Contact details            | Author(s) name and contact details.                                                                                                                        |
| Licensing/(re)use details  | Licence under which the materials are shared, and rules/conditions for (re)use and contribution.                                                           |
| Preferred citation         | Instructions on how to cite your material.                                                                                                                 |
| Description                | Overview of the subject matter, aims of the training and the language in which the training is delivered.                                                  |
| Learning outcomes          | Statements that indicate what trainees should be able to do upon successful completion of the training.                                                    |
| Target audience            | The intended audience, their prerequisite knowledge/skills, their general background, and how the training material will help them.                        |
| Required resources         | Technical resources and related materials (software requirements, datasets, infrastructure requirements, etc.).                                            |
| Keywords                   | Keywords or tags identifying the topic of the materials.                                                                                                   |
| Structure & duration       | Description of the structure of the materials and setting in which to deliver them, including the time allocated to each part (lectures, exercises, etc.)  |
| Additional information     | Items that provide additional information about (re)use and delivery of the materials (e.g., general tips/guidance).                                       |
| Links and references       | Links and references that are relevant to the content, but not required for delivery of the materials.                                                     |
| Date of last revision      | Date of last update of the materials, and the version.                                                                                                     |


For some of these categories the information is factual and it is obvious what to include (e.g. contact details, licence, date of last revision) but for other categories (e.g. learning outcomes, additional information) the content is more abstract and requires a little more thought.

For these more abstract categories, the quality, or richness, of the information provided is important for enabling reuse. For example, in our cake analogy, if your recipe only included the title “Best cake ever” and a list of ingredients “flour, eggs and milk” and instructions to “combine and bake” it would be difficult for someone to use the recipe to bake the same cake. Indeed they could end up with biscuits instead of a cake! At the same time there is a balance to be struck between providing enough information to be useful and too much overwhelming detail. 

Let’s look at ‘learning outcomes’ and ‘additional information’ in more detail.


!!! info "A word on keywords, ontologies and controlled vocabularies"

    Keywords are important for boosting the findability of training materials. Where possible, keywords should be chosen from an agreed upon list of terms (i.e an ontology or controlled vocabulary) that is relevant to your field. This helps ensure that keywords are used consistently and reduces ambiguity. For biology and bioinformatics [EDAM](https://edamontology.org/page) [@10.1093/bioinformatics/btt113] is an example of an ontology that includes agreed terms for data types, data identifiers, data formats, operations, and topics and you can use services like the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/index) to look up terms and keywords. 

    You can learn more about ontologies in this [video from the EMBL-EBI](https://www.ebi.ac.uk/training/online/courses/biocuration-collection/ontologies/).


## Writing learning outcomes

Writing learning outcomes in a consistent format makes them easier to understand and compare across different materials and sessions. These statements help trainees to determine if the training session is right for them. Trainers can also use them to determine if training materials cover the topics they wish to teach and if they are pitched at an appropriate level.

A bonus to writing learning outcomes is that it can help you define the purpose, intended audience  of your training session and what participants need to know (the prerequisites) before joining it.

!!! example "Learning experience: writing learning outcomes"

    1. Watch this video on [how to write SMART learning outcomes](https://drive.google.com/file/d/1T078jh5wWD5k5CdN1tf-YldXdyXZ3FnR/view?usp=sharing)
    
    <iframe src="https://drive.google.com/file/d/1T078jh5wWD5k5CdN1tf-YldXdyXZ3FnR/preview" width="320" height="240" allow="autoplay"></iframe>
    
    2. Now write a set of learning outcomes for your own materials. 
    3. Share your learning outcomes with a friend. Are they able to tell what the goals of your training are?


## Providing additional contextual information

Providing context about the delivery method helps other trainers** **plan for reuse. It’s also really useful if you have to repeat the same session sometime in the future! 

These are the things that come under ‘Required resources’, ‘Structure and duration’ and ‘Additional notes’ in the table.

For example, were these materials part of a workshop? Was the training delivered online or in person? How much time is needed for each activity? Was special software needed?

!!! example "Learning experience: adding contextual information"

    1. Find some examples of ways in which trainers provide ‘additional information’ and context about how to use training materials.
    2. How did they include this information?
    3. What information did they include?

There are several ways to include additional information. For example [Carpentries lessons](https://swcarpentry.github.io/shell-novice/) include ‘Instructor notes’ while [this example from the Swiss Institute of Bioinformatics](https://github.com/sib-swiss/first-steps-with-python-training/) uses a README file in their GitHub repository to collate this information and the [Australian BioCommons](https://zenodo.org/record/6350808#.YqfKV-xBw3Q) provides information in a table of metadata. You might even consider adding an extra slide to your slide deck when you share it.  In fact what you include and how, really depends on the materials and training session in question. To write your own notes, start by thinking of this as a training love letter to yourself. If you were to reuse these materials in 2, 5, 10 years time, what else would you need to know about the session?

It can be tempting to include a lot of detailed information here. Remember that you can also facilitate reuse of your materials by welcoming contributions and inviting people to get in touch if they need more information.


## How and where to share metadata

Recipes are typically written in a similar format that includes a photo of the dish alongside detailed metadata including i) a description ii) a list of ingredients iii) method/instructions. This makes it easy to quickly check if that recipe is right for you.

The same is true for training materials. Sharing metadata alongside your training materials makes it quicker and easier to review the materials. How you share this metadata depends on where you are sharing it. For example, repositories such as Zenodo prompt you to add metadata by providing a form for you to fill in when you upload your materials. If your repository is not specialised for training materials or doesn’t provide a form it may be necessary to add additional information in a free text format such as a README file. 

Whichever format you choose, use a consistent method for all of your training materials. This will save you time and make it easier to find, compare and contrast materials.

!!! info "Structuring metadata for machines"
    Metadata can also be structured to help machines search and catalogue this information. For more on this see [Chapter 4](https://elixir-fair-training.github.io/FAIR-training-handbook/chapters/chapter_04/).

Now it’s your turn to write a training recipe.

!!! example "Learning experience: Write your own training recipe"

    1. Make a table of the types of information you need to include in your metadata (you may wish to use the table above for inspiration). 
    2. Complete the table for your training material providing detailed information.
    3. Ask a friend to read your recipe. Do they have enough information to understand the materials and the context they were used in?

Here are some recommendations to help get you started:



* Create a templates to help you remember which information to include and to ensure consistency
* Write learning outcomes in a SMART format
* Include contextual information

**Examples of ways in which information about training materials can be shared**



* [Galaxy 101 for everyone](https://training.galaxyproject.org/training-material/topics/introduction/tutorials/galaxy-intro-101-everyone/tutorial.html) 
* [Australian BioCommons Materials](https://zenodo.org/record/6350808#.YqfKV-xBw3Q) (PDF metadata table)
* [Carpentries lesson](https://swcarpentry.github.io/shell-novice/) (Instructor notes)
* [SIB First steps with Python in Life Sciences](https://github.com/sib-swiss/first-steps-with-python-training/) (README file)
* A training dataset/Slide deck

!!! Checklist

    * Collate metadata

    * Share metadata alongside the materials

    * Write learning outcomes in a SMART format

    * Include detailed but brief information in the metadata to allow others to understand the context in which the training materials were originally used.

    * Choose keywords from an ontology or controlled vocabulary that is relevant to your field

## Resources and references
\bibliography

