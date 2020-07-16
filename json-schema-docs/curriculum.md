# Curriculum Schema

```txt
http://www.w3id.org/openeduhub/schema/curriculum-schema#
```

A generic JSON schema for describing school curricula


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                         |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [curriculum.schema.json](../../../jsonschema2md/out/curriculum.schema.json "open original schema") |

## Curriculum Type

`object` ([Curriculum](curriculum.md))

## Curriculum Default Value

The default value is:

```json
{
  "@context": {
    "id": "@id",
    "type": "@type",
    "@vocab": "http://schema.org/"
  }
}
```

# Curriculum Properties

| Property                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                           |
| :---------------------------------------- | -------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                                 | `string` | Optional | cannot be null | [Curriculum](curriculum-properties-url.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/id")                                                            |
| [type](#type)                             | `string` | Optional | cannot be null | [Curriculum](curriculum-properties-type-of-item.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/type")                                                 |
| [name](#name)                             | `string` | Optional | cannot be null | [Curriculum](curriculum-properties-name-if-the-item.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/name")                                             |
| [description](#description)               | `string` | Optional | cannot be null | [Curriculum](curriculum-properties-description.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/description")                                           |
| [creator](#creator)                       | `array`  | Optional | cannot be null | [Curriculum](curriculum-properties-creator.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/creator")                                                   |
| [courseCode](#courseCode)                 | `array`  | Optional | cannot be null | [Curriculum](curriculum-properties-course-code.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/courseCode")                                            |
| [educationalLevel](#educationalLevel)     | `object` | Optional | cannot be null | [Curriculum](curriculum-properties-educational-level-for-the-item.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/educationalLevel")                   |
| [educationalContext](#educationalContext) | `object` | Optional | cannot be null | [Curriculum](curriculum-properties-educational-context-bildungsstufe-for-the-item.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/educationalContext") |
| [hasPart](#hasPart)                       | `array`  | Optional | cannot be null | [Curriculum](curriculum-properties-subelements-of-item.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/hasPart")                                       |
| [license](#license)                       | `string` | Optional | cannot be null | [Curriculum](curriculum-properties-license.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/license")                                                   |

## id




`id`

-   is optional
-   Type: `string` ([URL](curriculum-properties-url.md))
-   cannot be null
-   defined in: [Curriculum](curriculum-properties-url.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/id")

### id Type

`string` ([URL](curriculum-properties-url.md))

### id Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc4291 "check the specification")

## type

Must be of type "Course"


`type`

-   is optional
-   Type: `string` ([Type of item](curriculum-properties-type-of-item.md))
-   cannot be null
-   defined in: [Curriculum](curriculum-properties-type-of-item.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/type")

### type Type

`string` ([Type of item](curriculum-properties-type-of-item.md))

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | ----------- |
| `"Course"` |             |

## name

Name of the Curriculum


`name`

-   is optional
-   Type: `string` ([Name if the item](curriculum-properties-name-if-the-item.md))
-   cannot be null
-   defined in: [Curriculum](curriculum-properties-name-if-the-item.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/name")

### name Type

`string` ([Name if the item](curriculum-properties-name-if-the-item.md))

## description




`description`

-   is optional
-   Type: `string` ([Description](curriculum-properties-description.md))
-   cannot be null
-   defined in: [Curriculum](curriculum-properties-description.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/description")

### description Type

`string` ([Description](curriculum-properties-description.md))

## creator




`creator`

-   is optional
-   Type: unknown\[]
-   cannot be null
-   defined in: [Curriculum](curriculum-properties-creator.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/creator")

### creator Type

unknown\[]

## courseCode




`courseCode`

-   is optional
-   Type: `string[]`
-   cannot be null
-   defined in: [Curriculum](curriculum-properties-course-code.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/courseCode")

### courseCode Type

`string[]`

## educationalLevel




`educationalLevel`

-   is optional
-   Type: `object` ([Educational level for the item](curriculum-properties-educational-level-for-the-item.md))
-   cannot be null
-   defined in: [Curriculum](curriculum-properties-educational-level-for-the-item.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/educationalLevel")

### educationalLevel Type

`object` ([Educational level for the item](curriculum-properties-educational-level-for-the-item.md))

## educationalContext




`educationalContext`

-   is optional
-   Type: `object` ([Educational context (Bildungsstufe) for the item](curriculum-properties-educational-context-bildungsstufe-for-the-item.md))
-   cannot be null
-   defined in: [Curriculum](curriculum-properties-educational-context-bildungsstufe-for-the-item.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/educationalContext")

### educationalContext Type

`object` ([Educational context (Bildungsstufe) for the item](curriculum-properties-educational-context-bildungsstufe-for-the-item.md))

## hasPart




`hasPart`

-   is optional
-   Type: unknown\[]
-   cannot be null
-   defined in: [Curriculum](curriculum-properties-subelements-of-item.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/hasPart")

### hasPart Type

unknown\[]

## license




`license`

-   is optional
-   Type: `string` ([License](curriculum-properties-license.md))
-   cannot be null
-   defined in: [Curriculum](curriculum-properties-license.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/license")

### license Type

`string` ([License](curriculum-properties-license.md))

### license Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^https://creativecommons.org/(licenses|licences|publicdomain)/.*
```

[try pattern](https://regexr.com/?expression=%5Ehttps%3A%2F%2Fcreativecommons.org%2F(licenses%7Clicences%7Cpublicdomain)%2F.* "try regular expression with regexr.com")

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc4291 "check the specification")
