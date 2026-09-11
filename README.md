# Fernando Ferraz — Online CV

This repository contains the source code for the online CV of **Fernando Jose M F Ferraz**.

The website presents a professional profile focused on:

- Data Analytics
- Finance Analytics
- AWS Cloud
- Cloud FinOps
- Finance and Accounting

## Live website

[docfferraz.site](https://docfferraz.site)

## Contents

| File | Purpose |
| --- | --- |
| `index.html` | The complete responsive CV website, including HTML, CSS and JavaScript. |

## Profile highlights

- Data and finance background, including economics, accounting and business operations
- AWS Certified Solutions Architect – Associate
- AWS Certified Cloud Practitioner
- AAT Level 3 Diploma in Accounting
- Skills in SQL, Python, Power BI, Tableau, Excel, AWS and Cloud FinOps

## Updating the website

1. Edit or replace `index.html` in this repository.
2. Commit the change to GitHub.
3. Upload the same `index.html` to the root of the AWS S3 bucket that hosts the website.
4. If the site uses Amazon CloudFront, create an invalidation for `/index.html` so visitors receive the latest version.

The filename must remain exactly `index.html` (lowercase), as it is the website's default page.

## Contact form and visitor counter

The website uses:

- Formspree for the contact form
- An AWS API endpoint for the visitor counter

Both are configured directly in `index.html`.

## Local preview

Download the repository and open `index.html` in a web browser. Most content will display locally; the visitor count and contact form require an internet connection.

## Licence

This repository contains personal CV content. Do not reuse its text, images or personal contact details without permission.
