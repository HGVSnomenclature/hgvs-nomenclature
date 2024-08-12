# How to release a new version of HGVS Nomenclature

This document describes how to release a new version of hgvs-nomenclature.org.  You must be a repo maintainer to use these instructions.

## Overview

A release is made by tagging the repo with a version tag of the form x.y.z (with
no v. prefix).  That operation alone is sufficient to cause Read the Docs to
rebuild the documentation as that version *and* to update the `/stable` link
(i.e., https://hgvs-nomenclature.org/stable/).

**The release notes under [HGVS Nomenclature
Version](https://hgvs-nomenclature.org/versions/) is now generated automatically
using exactly the same text as that in the GitHub release notes.**


## Instructions

1. Navigate to https://github.com/HGVSnomenclature/hgvs-nomenclature/releases.

1. Click **Draft a new release**.

1. Click Choose a tag and type the next tag.  See https://hgvs-nomenclature.org/stable/versions/ for our versioning policy.
![Choose tag](images/choose-tag.png)

1. Click **Generate release notes**. Proofread and edit the notes as you like.

1. Click **Publish release**.  The site should be regenerated within a few minutes.
