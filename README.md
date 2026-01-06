# Online CV – Static Website

This website serves as my professional and academic CV.

## Overview
The site is built as a lightweight static website to showcase my background,
skills, and experience in a clear and accessible format.

## Technologies Used
- HTML and CSS for structure and styling
- Amazon S3 for static website hosting
- Amazon CloudFront for global content delivery and HTTPS
- AWS Certificate Manager (ACM) for SSL/TLS certificates
- Amazon Route 53 for DNS management

## Architecture
HTML/CSS files are stored in an Amazon S3 bucket configured for static website hosting.
The site is delivered through an Amazon CloudFront distribution secured with an SSL
certificate from AWS Certificate Manager. Amazon Route 53 is used to manage DNS records
and route traffic to CloudFront.

## Deployment
Updates to the CV are made by editing the HTML/CSS files locally and uploading the
updated files to the hosting repository or S3 bucket. Changes are automatically served
through CloudFront.

