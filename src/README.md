# Rumus

## Perumusan TA FPIK

```md
<potongan gambar>

<rumus>
```

## Menyesuaikan Rumus TA FPIK dengan field CSL dan borang pengelola referensi

| Rumus        | Field  | Borang |
| ------------ | ------ | ------ |
| Nama Penulis | Author | Author |
|              |        |        |

# What Changed from APA

1. Name and UUID

1. Remove parentheses for year

1. Remove aqure brackets for description-thesis

2. "et al" as et al instead dkk. at:
```xml
  <locale xml:lang="id">
    <terms>
      <term name="et-al">et al.</term>
    </terms>
  </locale>
```

1. Bolded volume at:
```xml
<text font-weight="bold" variable="volume"/>`
```

1. publisher-place for thesis at:
```xml
  <macro name="description-thesis">
...
              <text variable="publisher"/>
              <text variable="publisher-place"/> < - - - here
```

1. publisher-place for book and other type:
```xml
...
        <!- - monographic types - ->
            <group delimiter=", ">
              <text variable="publisher"/>
              <text variable="publisher-place"/> < - - - here
            </group>
...
      <else>
          <group delimiter=", ">
            <text variable="publisher"/>
            <text variable="publisher-place"/> < - - - here
          </group>
      </else>
    </choose>
  </macro>
```