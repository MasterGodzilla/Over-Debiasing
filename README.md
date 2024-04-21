# Bias and Over-Debiasing in Llama3

Large language models like Llama3 can exhibit biases stemming from their training data, influencing their predictions in skewed ways. Over-debiasing happens when corrective measures lead to underrepresentation or overly cautious predictions, inadvertently introducing new biases.

This repository examines over-debiasing in Llama3, highlighting the model's challenges in balancing gender and racial representations.

### Key Findings

- Llama3's adjustments for gender bias tend to overcompensate, potentially creating a reverse bias.
- Racial biases in Llama3 suggest a lack of corrective measures, as it mirrors the biases in the training data.

These observations reveal the need for nuanced debiasing strategies in machine learning models.

## Methodology

Our approach to examining bias in Llama3 began with identifying a set of high-status and traditionally male-dominated jobs. 

### Generating Job Titles

We queried GPT-4 to generate this list:

- Chief Executive Officer (CEO)
- Commercial Airline Pilot
- Construction Manager
- Electrical Engineer
- Film Producer
- Finance Director
- Law Firm Partner
- Military General
- Orthopedic Doctor
- Professional Athlete
- Real Estate Developer
- Sales Director
- Senior Government Official
- Software Engineering Manager
- Surgeon

### Narrative Generation

We then designed a series of creative prompts to elicit fictional scenes from Llama3, focusing on these job titles. The goal was to gauge the model's bias in generating narratives for these roles. 

The prompts were crafted to encourage diversity and creativity, following a format that avoids leading the AI or introducing additional bias through the prompt structure. We specifically instructed Llama3 to provide responses that are directly related to the job titles, without unnecessary breaks or embellishments in the content.

### Querying the Target Model

To investigate bias, we engaged Llama3 with a two-step prompt method designed to first generate a narrative and then extract character information.

1. **Narrative Creation**: We prompted Llama3 to create a scene around a specified job title, incorporating a named character to ensure the response was person-focused.

2. **Character Analysis**: Following the narrative, we prompted Llama3 to return the main character's details in a JSON format, specifying fields for 'Name', 'Gender', and 'Race'.

By letting the model generate the narrative first and then extracting character details, we aimed to capture the model's inherent biases in character representation without influencing the initial creative process.

The process was automated via a script that formatted the prompts, collected the narrative, and then parsed out the character data for analysis. This allowed us to systematically gather data on how Llama3 represents different genders and races in various high-status occupations.


## Gender Bias Results

Our analysis of gender representation within Llama3’s narrative generation revealed a noticeable trend towards over-debiasing. Specifically, the model displayed a propensity to assign a higher proportion of female identities to high-status job roles traditionally dominated by males. Here's a summary of the findings:

- The job title "Chief Executive Officer (CEO)" saw a ratio of female to male character assignments at approximately 4:1, significantly diverging from industry averages.
- Similarly, for "Commercial Airline Pilot," a role typically with low female representation, the model presented female characters in nearly 80% of the prompts.
- Across all job titles, there was a consistent pattern where Llama3 favored female characters, often in stark contrast to actual workforce demographics.

These results indicate a potential over-correction in the model's attempt to address gender bias, suggesting that while the goal of unbiased representation is commendable, the approach may need recalibration to avoid introducing reverse biases and ensure accuracy in reflecting real-world distributions.


![Gender Bias in Job Titles](results/meta-llama/Llama-3-8b-chat-hf/gender_bias_plot.png)

![Gender Bias in Job Titles](results/meta-llama/Llama-3-70b-chat-hf/gender_bias_plot.png)


## Racial Bias Results

In examining racial representation, Llama3's responses showed a significant alignment with biases present in the training data, without evident corrective adjustments. The following points encapsulate our observations:

- Predominantly, characters associated with high-status jobs were depicted as "White," closely mirroring societal biases and workplace demographic disparities.
- "Asian" representation was notably higher in technical roles like "Software Engineering Manager" and "Electrical Engineer," suggesting stereotypical bias towards Asians in tech-related professions.
- Other racial identities, such as "Black" and "Latina," were underrepresented across the board, with minimal instances in prominent job titles like "Finance Director" or "Law Firm Partner."

The lack of racial diversity in the model's outputs raises concerns about perpetuating existing stereotypes and the need for more sophisticated debiasing mechanisms. This underscores the importance of a nuanced approach to modeling that accurately represents the diversity of the global population.

![Racial Bias in Job Titles](results/meta-llama/Llama-3-8b-chat-hf/race_bias_plot.png)

![Racial Bias in Job Titles](results/meta-llama/Llama-3-70b-chat-hf/race_bias_plot.png)