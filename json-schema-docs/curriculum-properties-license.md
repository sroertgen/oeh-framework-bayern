# License Schema

```txt
http://www.w3id.org/openeduhub/schema/curriculum-schema##/properties/license
```




| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | ---------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [curriculum.schema.json\*](../../../jsonschema2md/out/curriculum.schema.json "open original schema") |

## license Type

`string` ([License](curriculum-properties-license.md))

## license Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^https://creativecommons.org/(licenses|licences|publicdomain)/.*
```

[try pattern](https://regexr.com/?expression=%5Ehttps%3A%2F%2Fcreativecommons.org%2F(licenses%7Clicences%7Cpublicdomain)%2F.* "try regular expression with regexr.com")

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc4291 "check the specification")
