## Introduction to Weaviate - Online Workshop

This repository contains files related to the "Introduction to Weaviate" workshops, which we run periodically for an enthusiastic audience.

The repository is live, and will be updated with new content as we run more workshops and iterate from your feedback.

You can run the code using an online environment such as Google Colab, or locally.

## Key files

The notebooks are as follows:

- `workshop.ipynb`: For the audience to follow along with the instructor
- `workshop-complete.ipynb`: A completed version of the above notebook
- `z_optional_explain_vectors.ipynb`: An optional notebook for explaining how vectors represent meaning

### For instructors

- `generate_student_notebook.py`:
    - Run this to create a student version of the notebook `workshop.ipynb` from `workshop-complete.ipynb`.
    - Strips sections of cells between `# BEGIN_SOLUTION` & `# END_SOLUTION` and replaces it with `# ADD YOUR CODE HERE`.

### Weaviate Cloud Services

Some of the workshop code and examples are written around Weaviate Cloud (WCD).
You can sign up to WCS and create a free sandbox instance at `https://console.weaviate.cloud`.
