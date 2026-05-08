# Paritta — Back Template

```html
{{FrontSide}}

<hr id=answer>

<table>

    {{#marks}}
    <tr valign="top">
        <td class="another_color">My notes:</td>
        <td class="another_color"><i>{{marks}}</i></td>
    </tr>
    {{/marks}}

    <tr valign="top">
        <td class="another_color">Grammar:</td>
        <td>{{grammar}}</td>
    </tr>

    <tr valign="top">
        <td class="another_color">Meaning:</td>
        <td><b>{{meaning}}</b>{{#meaning_lit}}; lit. {{meaning_lit}}{{/meaning_lit}}</td>
    </tr>

    {{#root}}
    <tr valign="top">
        <td class="another_color">Root:</td>
        <td>{{root}}{{root_group}} {{root_sign}} ({{root_meaning}})</td>
    </tr>
    {{/root}}

    {{#root_base}}
    <tr valign="top">
        <td class="another_color">Base:</td>
        <td>{{root_base}}</td>
    </tr>
    {{/root_base}}

    {{#construction}}
    <tr valign="top">
        <td class="another_color">Constr.:</td>
        <td>{{construction}}</td>
    </tr>
    {{/construction}}

</table>

<hr>
<div class="small">{{feedback}}</div>

<span class="spacer"></span>

```
