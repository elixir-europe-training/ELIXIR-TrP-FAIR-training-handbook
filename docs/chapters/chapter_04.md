---
tags:
    - Metadata
    - Controlled vocabularies
    - Annotation
    - FAIR
    - Bioschemas
---

!!! Checklist  

    4.1 Choose a metadata standard used by your community - Bioschemas or RDA.
    4.2 Describe your training material using the properties of that metadata standard.
    4.3 Add the metadata into a README file, with the materials, or in the HTML/GitHub page where your training materials can be found, or within the training material itself (a ppt or pdf for instance).
    4.4 Use a validator to check the metadata you added.

## Description
Metadata can be defined as data used to describe _other data_. That _other data_ is complete on its own even without the metadata; however, the metadata makes it easier, for instance, to quickly grasp what that _other data_ is about and to establish some common parameters that can be used to find and compare similar data, even if you have no access to that _other data_. This chapter will focus on explaining how to annotate training materials and events with rich metadata to improve their Findability, Interoperability, and Reusability.

!!! info "Learning outcomes"
    **At the end of this chapter you should be able to:**

    1. Explain the concept of metadata 
    2. Explain the relevance of metadata to FAIR Training Materials
    3. Identify metadata standards used in your communities/institutions to annotate training materials
    4. Explain the concept of structured metadata (optional)
<!---
Recommended, Apply - Describe their training materials with a metadata standard suitable for their domain/discipline (note: from the point of view of content, this could be a LE. bring your TrM, and structure/insert/compile the metadata)
--->

## Prerequisites
* Understand what is FAIR and why to use it as explained in [Chapter 1: Why FAIR training & training materials?](https://elixir-fair-training.github.io/FAIR-training-handbook/chapters/chapter_01/)

## Introduction to metadata

Metadata can be defined as data used to describe *other data*. That *other data* is complete on its own even without the metadata; however, the metadata makes it easier, for instance, to quickly grasp what that *other data* is about and to establish some common parameters that can be used to find and compare similar data, even if you have no access to that *other data*. As examples might be easier to grasp than definitions, let’s have a look at a couple of metadata examples:

* You look at a can (data) of a new beverage and later comment this with a friend who wants to know more. You do not remember the name (metadata) of the beverage, but you tell your friend about the height and colours of the can (metadata). Your friend quickly realises what that new beverage is as she has already tried it out.
* You can read, enjoy and learn from a book (data) even if you do not know the title, the author, or the date it was printed (metadata). However, if you really like that book and know the name of the author, you can also find other books by the same author.
* You look for a film (data) in your preferred browser. As you know the title (metadata) you can easily find not only the film (access is restricted to those renting the film) but information about the director and the actors, and even a summary of the plot (more metadata).
* You are interested in finding concerts happening during summer. You go to your preferred browser and use some keywords (metadata) to find some concerts close to your city.

Most likely, you have already used metadata without even noticing it!

While the first example involved only people, the other three involved people and machines. When we want to communicate with other people, we use words, either orally or written and thanks to the common knowledge of the used language, e.g., English, we can understand each other. A sentence like ‘the title of this chapter is “Using metadata to describe training materials” ‘ is clear for us, but while free text is enough for humans, machines need more structured data (and metadata) to communicate with each other. The sort of structured metadata we use to describe training materials looks like a sentence with a subject, a predicate, and an object, with the main subject being our training material. The sentence above would for example look like: thisChapter (subject) - hasTitle (predicate) - “Using metadata to describe training materials”. Further information about how we communicate with machines and how machines communicate with each other is an exciting subject, but it is outside the scope of this book. If you are interested, we offer some additional information in Section [Further reading about structured metadata](#FR).

## Why do we need to describe training materials with metadata?

Metadata will improve F, I, R

## Metadata for training materials

Metadata will help us describe our training materials, but what metadata should we use? If we all decide on our own what metadata we want to use and how it will look in its machine-readable version (i.e., structured metadata via schemas), we will end up with so many ways to refer to what should be common ground (so we understand better each other, humans and machines). Rather than going on your own, we recommend you find and follow a metadata standard used by your community (e.g., trainers in general or trainers in your field and/or in your institute). We are aware of a couple of communities working on training materials and supporting metadata for them; they are [GOBLET](https://www.mygoblet.org/), [ELIXIR](https://elixir-europe.org) Training Platform (particularly the FAIR Training Focus Group) and the Research Data Alliance via its [Education and Training on Handling of Research Data Interest Group](https://www.rd-alliance.org/groups/education-and-training-handling-research-data.html) (RDA-ETHRD-IG).

[GOBLET](https://www.mygoblet.org/) is the Global Organisation for Bioinformatics Learning, Education and Training. Its mission is to cultivate the global bioinformatics trainer community, set standards and provide high-quality resources to support learning, education and training. [ELIXIR Europe](https://elixir-europe.org) is an intergovernmental organisation that brings together life science resources from across Europe. These resources include databases, software tools, training materials, cloud storage and supercomputers. [RDA-ETHRD-IG](https://www.rd-alliance.org/groups/education-and-training-handling-research-data.html) is one of the Interest Groups of the Research Data Alliance established to face the increasing volumes of data created by researchers and the need of specific skills to handle them. It aims at creating taxonomies of those skills and elaborate reference models. It will enable the setting of quality standards in this education field, encourage the recognition of the skills and prepare the ground for practical applications when applying these standards. It has around 300 members.

A first proposal for recommended metadata for training materials was published in the [10SR paper](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007854#sec003) in [table 2](https://doi.org/10.1371/journal.pcbi.1007854.t002).

### Bioschemas

GOBLET and ELIXIR have worked together on the subject of metadata for training materials under a community-based project umbrella, namely Bioschemas. Bioschemas [@Bioschemas] is a collaborative effort supporting metadata schemas to describe types relevant in the Life Sciences domain (e.g., Gene and Protein) and providing guidelines (known as profiles) on how to use general-purpose types offered by Schema.org (e.g., Dataset or Learning Resource). Schema.org [@Schema] is also a collaborative effort providing cross-domain types with the purpose of adding structured markup to web pages so web search engines understand better what they are about.

There are three Bioschemas profiles related to training: [Course](https://bioschemas.org/profiles/Course/1.0-RELEASE), [CourseInstance](https://bioschemas.org/profiles/CourseInstance/1.0-RELEASE) and [TrainingMaterial](https://bioschemas.org/profiles/TrainingMaterial/1.0-RELEASE). Each profile contains sets of properties that are either Minimum (mandatory), Recommended or Optional. TrainingMaterial properties cover attributes like name, description, and language of the material, time required to work through it, contributors, version, etc.

## Metadata in action - case studies

1. Metadata in GitHub pages: [How Bioschemas uses the training profiles with GitHub pages and Jekyll](https://bioschemas.org/tutorials/community/training)

2. Metadata in html pages: metadata will usually be in the \<head\> part between \<script\> tags of type "application/ld+json"

    *Example*: [Basic proteomics course instance](https://training.vib.be/all-trainings/basic-proteomics-0) - Right-click => Inspect to see the html code


There are validators and viewers of metadata available:

* [Schema validator](https://validator.schema.org)
* [JSON-LD viewer](http://jsonviewer.stack.hu)
* [JSON-LD playground](https://json-ld.org/playground/)

!!! example Metadata in action - hands-on
    Describe one of your training materials with a metadata standard suitable for your domain/discipline

## <a id="FR"></a> Further reading about structured metadata

If you are here, you want to know a bit more on how machines communicate with each other. As we said before, while free text is enough for humans, more structured data (and metadata) works better with machines. Data can be structured in many ways (most of them also outside the scope of this book). We will focus on the sort of metadata using sentences to describe things in a light way, i.e., metadata 

s. There is still much more around this topic including semantics, controlled vocabularies, terminologies and ontologies, all of that outside the scope of this book.

## Resources and references

\bibliography
