# Introduction and Goals

Es soll eine Bibliothek erstellt werden mit der well-formed Markdown-Code erzeugt (Schritt 1) und wieder eingelesen (Schritt 2) werden kann.

## Requirements Overview

The requirements are stored in a YAML file. Each requirement is described in its own section and uniquely numbered. The file is saved in the directory [doc/arc42/requirements.yaml](requirements.yaml).

### Example of a Requirement

```yaml
requirements:
    Req.1:
        description: The library must be able to generate well-formed Markdown code.
        acceptance_criteria:
            - The generated Markdown code must comply with common standards.
        priority: High
```

### Testing the Requirements

The requirements are verified through unit tests and integration tests. The tests are implemented using a test framework like `pytest` and stored in the directory `/y:/workspace/_project/_private/Markdown/tests/`. Each requirement is covered by at least one test case.

### Example of a Test Case

```python
def test_markdown_generation():
        generator = MarkdownGenerator()
        result = generator.generate_code()
        assert is_well_formed_markdown(result), "The generated Markdown code is not well-formed"
```

## Quality Goals

## Stakeholders

| Role/Name   | Contact        | Expectations       |
| ----------- | -------------- | ------------------ |
| *\<Role-1>* | *\<Contact-1>* | *\<Expectation-1>* |
| *\<Role-2>* | *\<Contact-2>* | *\<Expectation-2>* |

# Architecture Constraints

# Context and Scope

## Business Context

**\<Diagram or Table>**

**\<optionally: Explanation of external domain interfaces>**

## Technical Context

**\<Diagram or Table>**

**\<optionally: Explanation of technical interfaces>**

**\<Mapping Input/Output to Channels>**

# Solution Strategy

# Building Block View

## Whitebox Overall System

***\<Overview Diagram>***

## Class Diagram

```mermaid
classDiagram

    class MarkdownGenerator {
        +generate_code()
        +read_code()
    }

    class CodeBlock {
        +content: str
        +format()
    }

    class Heading {
        +level: int
        +text: str
        +format()
    }

    class Paragraph {
        +text: str
        +format()
    }

    class Blockquote {
        +text: str
        +format()
    }

    class List {
        +items: list
        +ordered: bool
        +format()
    }

    class Link {
        +url: str
        +text: str
        +format()
    }

    MarkdownGenerator --> CodeBlock
    MarkdownGenerator --> Heading
    MarkdownGenerator --> Paragraph
    MarkdownGenerator --> Blockquote
    MarkdownGenerator --> List
    MarkdownGenerator --> Link
```


Motivation
*\<text explanation>*

Contained Building Blocks
*\<Description of contained building block (black boxes)>*

Important Interfaces
*\<Description of important interfaces>*

### \<Name black box 1>

*\<Purpose/Responsibility>*

*\<Interface(s)>*

*\<(Optional) Quality/Performance Characteristics>*

*\<(Optional) Directory/File Location>*

*\<(Optional) Fulfilled Requirements>*

*\<(optional) Open Issues/Problems/Risks>*

### \<Name black box 2>

*\<black box template>*

### \<Name black box n>

*\<black box template>*

### \<Name interface 1>

…

### \<Name interface m>

## Level 2

### White Box *\<building block 1>*

*\<white box template>*

### White Box *\<building block 2>*

*\<white box template>*

…

### White Box *\<building block m>*

*\<white box template>*

## Level 3

### White Box \<\_building block x.1\_\>

*\<white box template>*

### White Box \<\_building block x.2\_\>

*\<white box template>*

### White Box \<\_building block y.1\_\>

*\<white box template>*

# Runtime View

## \<Runtime Scenario 1>

-   *\<insert runtime diagram or textual description of the scenario>*

-   *\<insert description of the notable aspects of the interactions
    between the building block instances depicted in this diagram.>*

## \<Runtime Scenario 2>

## …

## \<Runtime Scenario n>

# Deployment View

## Infrastructure Level 1

***\<Overview Diagram>***

Motivation
*\<explanation in text form>*

Quality and/or Performance Features
*\<explanation in text form>*

Mapping of Building Blocks to Infrastructure
*\<description of the mapping>*

## Infrastructure Level 2

### *\<Infrastructure Element 1>*

*\<diagram + explanation>*

### *\<Infrastructure Element 2>*

*\<diagram + explanation>*

…

### *\<Infrastructure Element n>*

*\<diagram + explanation>*

# Cross-cutting Concepts

## *\<Concept 1>*

*\<explanation>*

## *\<Concept 2>*

*\<explanation>*

…

## *\<Concept n>*

*\<explanation>*

# Architecture Decisions

# Quality Requirements

## Quality Tree

## Quality Scenarios

# Risks and Technical Debts

# Glossary

| Term        | Definition        |
| ----------- | ----------------- |
| *\<Term-1>* | *\<definition-1>* |
| *\<Term-2>* | *\<definition-2>* |
