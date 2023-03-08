---
tags:
    - Training Development platform
    - Archiving
    - Collaborative development 
    - Repository
    - Version control
    - Content management
    - Technological platform
---


## Description
Here, we will describe a few platforms that can be used to host and share your materials in all four phases of their life cycle (development, delivery, sharing, and archiving), thus ensuring a higher degree of FAIRness. The platforms we will discuss are: Google Suite, GitHub and GitLab, Zenodo, Learning Management systems. We chose them as they are free, they include different features, and they are very commonly used in training. We will see which platforms are better to use in each phase of materials life cycle and why and what are the pros and cons of each platform according to FAIR principles.


!!! info "Learning outcomes"
    **At the end of this chapter you should be able to:**
    
    1. Describe the four phases of training materials life cycle (development, running course, sharing, archiving) 
    2. Describe why to use the Google Suite, GitHub/GitLab, Zenodo, a web portal and a Learning Management System (LMS) 
    3. List the (long-term) implications in terms of FAIR of choosing technologies such as Google Suite, GitHub/GitLab, Zenodo, a web portal and a Learning Management System (LMS)
    4. Compare the advantages and disadvantages of the platforms in each of the four phases
    5. For each phase, explain how to interpret FAIR principles
    6. For each phase, identify platforms that best comply with the FAIR principles according to user’s needs and priorities
    7. Document/justify your choices for a given learning platform
    8. Set up your training environment according to these guidelines

<!---    Optional Training objectives:
    1. Optional, Evaluate: Set up markdown driven training environments with continuous integration
--->

## Prerequisites

- Learners are expected to have done [Chapter 1](https://elixir-fair-training.github.io/FAIR-training-handbook/chapters/chapter_01/) and [Chapter 2](https://elixir-fair-training.github.io/FAIR-training-handbook/chapters/chapter_02/) and understand the need for FAIRifying their training materials and/or building their training materials FAIR from the beginning. 
- From [Chapter 2](https://elixir-fair-training.github.io/FAIR-training-handbook/chapters/chapter_02/), they are aware of what types of material they have or will have (lectures, exercises, video, datasets etc.). 

Learners may benefit from:

- being familiar with course design principles  / Nicholls cycle (tbc),
- having their lesson plan in place.

<!---
## Learning Experiences
#### LO: Describe the four phases of training materials life cycle (development, running course, sharing, archiving) 
1. Lecture describing the four phases of training materials life cycle. 
2. (Tentative) Exercise: learners describe what they currently do with their materials in each of the four phases. 

#### LO: Describe how to use the Google Suite, GitHub/GitLab, Zenodo, a web portal and a Learning Management System (LMS) 
1. Brief narrative presenting the different platforms
2. Exercise: learners share in groups which ones they will use / test quickly those they never used. 

#### LO: List the (long-term) implications in terms of FAIR of choosing technologies such as Google Suite, GitHub/GitLab, Zenodo, a web portal and a Learning Management System (LMS)
1. Exercise: in groups, learners discuss what could be the implications in terms of FAIR of choosing technologies such as Google Suite, GitHub/GitLab, Zenodo, a web portal and a Learning Management System (LMS) and write the outcomes of their discussion in a shared document (the document will contain a table listing the technologies in the first column and empty cells in the second column for the implications).  
2. Learners compare their table with the table provided in the chapter, where some possible implications are provided. 

#### LO: Compare the advantages and disadvantages of the platforms in each of the four phases
1. Exercise: in groups, learners write  the advantages and disadvantages of the platforms in each of the four phases in a shared Doc. They compare and discuss their results with the table “Pros & Cons” provided in the chapter.

#### LO: For each phase, explain how to interpret FAIR principles 
1. Narrative explaining the table structure and providing examples for each couple of dimensions
2. Exercise: Fill the Phases x FAIR table. 

#### LO: For each phase, identify platforms that best comply with the FAIR principles according to user’s needs and priorities
1. Brief narrative explaining why to focus on the user’s needs
2. Exercise: Highlight the more important columns of table 1.2 and 1.3 and fill those.

#### LO: Documenting/justifying their choices for a given learning platform
1. Exercise: justify the choice of one or multiple platforms.

--->

## Introduction

Once you have identified what learning experiences (lecture, hands on, exercises, work in groups, etc.), are needed to achieve the learning outcomes of your lesson / course and chosen the most appropriate and FAIR support(s) for the delivery of each of them (e.g. slide deck and/or video for the lecture, pdf for the hands on, shared notes for the work in groups, etc.), you should start considering where you will develop your materials (locally on your computer? or will you rather use a web platform/repository?), from where you will deliver them, how to share them with learners and how you will archive them for recognition and reuse by other instructors.

You might decide to develop your materials locally, on your computer, deliver them from your computer (e.g. projecting your local powerpoint), share them by email with learners and archive them on your hard disk and send them to other instructors by email upon request. Despite you might feel comfortable with this “old fashion” approach, you must be aware it is the least FAIR possible. FAIR principles will have a different degree of importance in each of the four phases of the material life cycle: development, delivery, sharing, and archiving. 

Here, we will describe a few platforms - Google Suite, GitHub and GitLab, Zenodo, Learning Management systems - that can be used to host and share your materials in all four phases of their life cycle,  thus ensuring a higher degree of FAIRness. We chose them because they are free, include different features, and are very commonly used in training. We will see which of those platforms is better to use in each phase of the materials life cycle and why and what are the pros and cons of each platform according to FAIR principles.

## The four phases of training materials life cycle

**Phase 1 - Development**

Development is the phase where you are designing and adding content to your training materials, ideally following the guide of the relative learning objectives and learning experiences. This might be a collaborative process, involving several lesson developers or a main developer and some contributors providing feedback. If you are developing your materials in collaboration, using an online platform in this phase may provide the essential advantage of allowing real-time collaboration (although not all the online platforms do), but there are other advantages linked to using an online platform, such as: the possibility to develop materials from anywhere at any time (for example, if your working laptop is not available), use the online resource as a backup strategy, the possibility to take advantage of the online resource feature to move the training materials to the following stages.

**Phase 2 - Delivery**

Delivery is the phase when, after developing your materials, you will run the course (with an actual audience). If you have training materials in the format of slide decks, this is the phase where you present them. If you have videos or written materials, this is the phase when learners consult them. Consider that: (1) this may happen at a specific time and with a specific schedule (during a few days course) or as self-paced learning. (2) This may require interactions with you as a trainer or between participants, or none, depending on the type of activities that you included in the course design. (3) The materials hosting platform may include built-in assessment of learning, or not (e.g. short multiple choice tests to allow progression to the next chapter). All these features must be taken into account while choosing the platform to support the training delivery. Whatever the format and the activities are, you should in parallel design a way to capture the learners’ feedback about the materials (another feature which may or may not be built-in to the platform used in delivery). Feedback will be essential in this phase to understand the level of maturity of the materials and enhance them. To allow changes to be made according to the received feedback, the platform you used in phase 1 should still be available to you. 

**Phase 3 - Sharing**

Depending on the type of content, some learners might benefit from accessing the materials even after the course ends, to consolidate their knowledge, to access optional information that you didn’t cover during the delivery, to (re)run some learning experiences, etc. The sharing phase is when you allow them to access the training materials asynchronously with the delivery phase: it might happen or not, but it should always happen in a FAIR process. We encourage you to consider the potential benefits of sharing the materials even before the delivery (e.g. to support some types of learners with impairments), but an extended discussion about this is beyond the current chapter’s scope. Similarly, we encourage you to consider sharing your materials with other audiences, e.g. potential contributors, other trainers, experts. Once they will get to know about your training materials (phase 3), you can allow them to access the platform where you design them (phase 1), which may or may not be the same, and contribute to them.  

**Phase 4 - Archiving**

As phase 3, archiving might not always happen. This is the case when you are not actively delivering a course anymore, or for various reasons you are not actively sharing the materials with learners and/or contributors (e.g. they are outdated), but you still want to keep an history of them and to support acknowledgment of who authored them in the past. In this phase, you should not need to be able to edit them, and you would rather “freeze” a specific version to be stored with extensive metadata about its contributors, when and where the course was delivered, and other information potentially useful for the trainers much more than for the learners. 

<img width="486" alt="Screenshot 2023-02-02 at 11 43 04" src="https://user-images.githubusercontent.com/8490781/216303440-0e38be75-ff99-44d7-b609-1cd9232519dc.png">

**Figure 3.1 A schematic representation of the training materials life cycle.** Dashed arrows mean that the following phase may or may not happen. Each phase cell also includes circles, indicating whose needs should the platform of choice mostly take into account (trainers or learners).

## Google Suite, GitHub/GitLab, Zenodo, a web portal and a Learning Management System (LMS) 

There are several platforms and systems out there, and we don’t have the intention to give an extensive and exhausting list of tools. We have chosen to focus on the following four systems because they are free, they are quite simple to use and are very commonly used in training, and also because they include different features that facilitate the FAIRness of materials:

- Google Suite is a Cloud share where people can also work collaboratively, organised in files and folders. It includes different types of documents (slides, sheets, docs). It automatically saves a history of edits for each file, versions can be named to bookmark significant stages. 
- GitHub and GitLab are git based platforms. Git is a version control system.  The common usage of the two platforms would be to sync a local repository with a remote one, which can in turn be cloned and synced from others. Git includes merging/branching/solving conflicts solutions that facilitate collaboration. GitHub and GitLab (the web platforms) include additional features like issues and actions (not covered in detail).
- Zenodo is a platform to upload materials of different formats and annotate them with metadata. Each upload corresponds to one version which once uploaded cannot be edited. Uploading to Zenodo allows the assignment of a DOI. 
- Learning management systems are applications to support the learning, sometimes including assessment and other personalised features. “Moodles” (e.g. Coursera) are LMSs. Usually they have standardised metadata and self-learning features. The materials are not always downloadable.

!!! example "Exercise"

    Think about / share in groups which ones you used in the past and test quickly those you never used to answer the following questions:
    - Do you need an account to access the platforms? Does your account need permissions to view someone else’s project?
    - How do you search for someone else’s project on the platform? Does the search include parameters, e.g. date of creation? 
    - How would you add a new project? Is there an option to make it private or accessible only to selected users?
    - In which of the four phases (development, delivery, sharing, archiving) will the platform “accept” your project? Multiple answers are possible.

## Long-term implications of choosing one of the platforms 

**section incomplete**

Depending on the phases of the training materials life-cycle, long term may mean different things. First ones are very short and mid-term bound (you have a course for a deadline). Archiving is long term.

By being free, we can’t ensure that these platforms will leave forever, but we may be confident that some will leave a …. Zenodo long term commitment from funders

When we think about long-term implications, the time frame can vary from some months to some years (2, 5, 10 years from now, or forever for the posterity). Some topics may live well for a long time. For instance, a course on UNIX will live well for many months and years, because the “language” does not vary frequently over time, and 10 years can still be a reasonable long-term goal. 

## Advantages and disadvantages of the platforms in each of the four phases

As anticipated in Figure 3.1, in different phases you might need to prioritise the needs of different types of audiences, and choose your platform accordingly. This should really be a case-by-case analysis and we don’t aim at covering all the possible needs in this analysis, but we will summarise in the following paragraph the most common features to take into account in choosing a platform for each of the different phases. We will treat each phase separately, but we acknowledge that you might want to prioritise some more than others to minimise the number of platforms used in the entire process. 

**In Phase 1, Design:**

- You probably want to choose a platform that facilitates collaborative editing of the training materials from multiple collaborators. Even if you start working as the sole author of your materials, consider that your community of authors will only grow if you design a structure that will facilitate contributions (this concept is extensively covered in other chapters of this handbook). In addition, you could look at yourself as a possible second contributor in the future: the more information you provide to guide your collaborators, the more information you will have when you get back to your project when months (or years) have passed  since the last time you edited the materials. 
- Consider this “information” (contribution guides, metadata about the materials, etc.) should be attached to the materials, easily reachable from them, but in principle it will not be included in the materials themselves (e.g. it’s not part of the slide deck content). For this reason, another important feature to consider is how clearly does the platform you choose create a link between your guide for trainers, or your metadata, and the actual training materials (Chapter 5 includes a more detailed analysis of this). 
- Finally, consider how easily the platform allows you to organise the training materials in modules. An extended discussion on modularisation of training (materials) goes beyond the scope of this chapter, however we would like to highlight that it will improve several aspects of FAIR. 

**In Phase 2, Delivery:**

- We would argue that during the course delivery you, together with all the trainers, are the main user of the training materials. When considering the platform to use during the delivery, prioritise the format and tools that simplify and support better the trainers. This will in turn ensure the best possible delivery quality. 
- Examples of questions to be asked in this regard are: are the trainees viewing the same information than the trainer does? E.g. do trainers need to visualise notes on the side? If so, how will the platform allow that? You probably want to minimise the channels splitting the attention of both the trainees and the trainers, providing them all the necessary information but not more. 
- Another set of questions can be: how easy should it be for trainers and trainees to live edit training materials during the course? Where and how will they follow practical activities? Do they need collaborative documents for that? And how and how long will they need to access the documents then?
- In this phase, keep accessibility and inclusivity in mind: e.g. will any of your learners be facilitated if you provide trascripts during an online lesson? 

**In Phase 3, Sharing:**

- Sharing will allow you to strengthen your training community, both in terms of increasing the number of trainers, facilitate their collaboration and reaching more trainees. In this phase, findability is to be prioritised, to ensure to be visible to a diversity of stakeholders. 
- Examples of questions to be asked in this context are: what is the platform to which your stakeholder audiences already have access, or the skills to navigate and search in it? Does the platform allow searching in the first place?
- Or additionally, will you allow download of the training materials and will learners be able to share them with peers independently? Would you allow that, or would you prefer all trainees to access them through the same platform, also for usage mapping?
- Finally, is there any additional information that learners need to access together with the materials? How will the platform you use support the link between multiple types of information sources, if that's the case (e.g. videos of your lessons and slides)? 
- A similar question for other potential trainers: do they need to access a trainers guide? How will you ensure that they are provided it, and if you plan to provide two different "trainers" and "learners" guides, how do you plan to guide them to the right document?

**In Phase 4, Archiving:**

- In this phase (if it happens), what you probably want is to secure an history of your training materials in a safe place, from where eventually others can access them. You are not aiming at enlarging the community of people that access them at this point, but consider that ensuring access from different institutitutions, for example, can become useful for you if you change your job position. Once again, everything you do to allow access to others can be useful to you in the future.
- Finally, consider that ensuring an archive of all your training materials creates demonstrators for your career development and your job applications, and your role as expert trainer in all other professional contexts. 

## The life-cycle of training materials and the FAIR principles 

Recap of the four phases:
- Materials development (collaborative or not),
- Consultation of the training materials by your learners during the course delivery,
- Sharing the training materials with learners and potential trainers after completion,
- Archiving the training materials to provide long-term reference.

Take into consideration that most of these platforms are not specifically designed for training materials.
The platforms shown are differently fit for the different phases, e.g. the Google Suite allows easy collaborative development but, because it is not possible to search for projects that our account is not linked to, it strongly limits the possibilities of sharing. 
Moreover, the platforms might support in different ways the FAIR principles (Findable, Accessible, Interoperable, Reusable) application to training materials, e.g. Zenodo supports findability of materials through rich metadata but the interoperability of these materials (how easy it is to modify, integrate or extend them) strongly depends on the format they are uploaded in. 
In turn, also the FAIR principles are differently applicable to the four phases, e.g. training materials being findable in the development phase implies being findable by other potential trainers interested in contributing to the development, while in the sharing phase implies being findable to other potential trainers interested in consulting them after completion, for reuse. 

Potentially, one could compile a three dimensional table to discuss this topic, where the dimensions are: the training platforms, the four letters of FAIR, and the four phases of a project development. In the cells, one could add considerations about if the two dimensions are one fit to the other, and why. The table, decomposed in three two-dimensional tables and pre-filled with the previous examples, could look as follows.  

**Table 1.1 Phases x Platforms**

| | Development | Running course | Sharing | Archiving |
| --- | --- | --- | --- | --- |
| Google Suite | YES, easy collaborative development, automatic backup and versioning | | NO, no way of searching training materials from others | |
| GitHub and GitLab | | | | |
| Zenodo | | | | |
| Coursera (LMSs) | | | | |

**Table 1.2 FAIR x Platforms**

| | Findable | Accessible | Interoperable | Reusable |
| --- | --- | --- | --- | --- |
| Google Suite | | | | |
| GitHub and GitLab | | | | |
| Zenodo | YES, rich metadata and search functions | | NO, if materials are uploaded in non-editable formats | |
| Coursera (LMSs) | | | | |
| Google Suite | | | | |

**Table 1.3 Phases x FAIR**

| | Development | Running course | Sharing | Archiving |
| --- | --- | --- | --- | --- |
| Findable | YES, if the aim is to involve other trainers in the development process | | YES, to allow other potential trainers to reuse the materials or students to access them after the course | |
| Accessible | | | | |
| Interoperable | | | | |
| Reusable | | | | |

!!! example "Exercise"

    Fill (alone or in groups) table 1.3, “Phases x FAIR”. 

In the discussion above, you might be more interested in considering a specific phase (because, for example, that’s the phase where your course is in) or a particular letter of FAIR (because, for example, you have been asked by your institution to improve that aspect of your training materials). You aim to understand which platforms would better comply with either one or the other, so focus on specific row(s) of the other two tables. There is not one solution that works for all cases. FAIRification is a process that starts from your priorities and implies adopting increasingly better practices to achieve them and enhance the quality of your training materials. 

!!! example "Exercise"

    Highlight the columns in tables 1.2 “Phases x Platforms” and 1.3 “FAIR x Platforms” that you consider more relevant for your specific case. Fill each column consulting all the platforms, especially those that you never used. 

!!! example "Exercise" 

    By looking at the tables you filled in the previous learning activity, choose one platform (or more, for different phases). Justify your choice by comparing the advantages and disadvantages of that platform with the others.

## Evaluate yourself

Now that you have completed the chapter, you should have reached the learning outcomes. Scroll up, and see whether you managed.

