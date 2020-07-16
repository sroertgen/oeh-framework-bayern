# Educational context (Bildungsstufe) for the item Schema

```txt
http://www.w3id.org/openeduhub/schema/curriculum-schema##/properties/educationalContext
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ---------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [curriculum.schema.json\*](../../../jsonschema2md/out/curriculum.schema.json "open original schema") |

## educationalContext Type

`object` ([Educational context (Bildungsstufe) for the item](curriculum-properties-educational-context-bildungsstufe-for-the-item.md))

# Educational context (Bildungsstufe) for the item Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                   |
| :-------------------- | -------- | -------- | -------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type)         | `string` | Optional | cannot be null | [Curriculum](curriculum-properties-educational-context-bildungsstufe-for-the-item-properties-type.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/educationalContext/properties/type")         |
| [id](#id)             | `string` | Optional | cannot be null | [Curriculum](curriculum-properties-educational-context-bildungsstufe-for-the-item-properties-id.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/educationalContext/properties/id")             |
| [inScheme](#inScheme) | `object` | Optional | cannot be null | [Curriculum](curriculum-properties-educational-context-bildungsstufe-for-the-item-properties-inscheme.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/educationalContext/properties/inScheme") |

## type




`type`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Curriculum](curriculum-properties-educational-context-bildungsstufe-for-the-item-properties-type.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/educationalContext/properties/type")

### type Type

`string`

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation |
| :---------- | ----------- |
| `"Concept"` |             |

## id




`id`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Curriculum](curriculum-properties-educational-context-bildungsstufe-for-the-item-properties-id.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/educationalContext/properties/id")

### id Type

`string`

### id Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc4291 "check the specification")

## inScheme




`inScheme`

-   is optional
-   Type: `object` ([Details](curriculum-properties-educational-context-bildungsstufe-for-the-item-properties-inscheme.md))
-   cannot be null
-   defined in: [Curriculum](curriculum-properties-educational-context-bildungsstufe-for-the-item-properties-inscheme.md "http&#x3A;//www.w3id.org/openeduhub/schema/curriculum-schema##/properties/educationalContext/properties/inScheme")

### inScheme Type

`object` ([Details](curriculum-properties-educational-context-bildungsstufe-for-the-item-properties-inscheme.md))
