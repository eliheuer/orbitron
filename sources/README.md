# Build Notes

Variable font is generated using Fontmake v1.5.0.dev0 using the following cli input: https://github.com/googlei18n/fontmake

```
fontmake -g Orbitron.glyphs -o variable
```

Prep and gasp tables have been created with a gftools script: https://github.com/googlefonts/tools/blob/master/bin/gftools-fix-nonhinting.py

DSGI table has been created by hand editing a ttx conversion.

```
  <DSIG>
    <!-- note that the Digital Signature will be invalid after recompilation! -->
    <tableHeader flag="0x0" numSigs="0" version="1"/>
  </DSIG>
```
