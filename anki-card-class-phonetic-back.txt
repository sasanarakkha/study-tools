{{FrontSide}}

<hr id=answer>

{{#marks}}

<div class=notesclass><i>{{marks}}</i></div>
<div class=brclass><br></div> 

{{/marks}}

{{#root}}

<div class=myclass> {{root}} </div>
<div class=brclass><br></div>
{{/root}}

<div class=myclass>
{{#base}} <b>{{base}}</b> <div class=brclass><br></div> {{/base}}<b>{{constr}}</b>
</div>

{{#phonetic}}
<div class=brclass><br></div>
<div class=myclass><div style='font-size: 80%;'>  <b><i>{{phonetic}}</i></b></div></div>
 {{/phonetic}}

{{#derivative}}
<div class=brclass><br></div>
<div style='font-size: 90%;'> <i>Deriv: </i> {{derivative}} ({{suffix}})
</div>
{{/derivative}}

<div class=brclass><br></div>

<div style='font-size: 85%;'>
<i>{{pos}}{{#gram}}, {{gram}}{{/gram}}{{#derived}}, from  {{derived}}{{/derived}}{{#neg}}, {{neg}}{{/neg}}{{#verb}}, {{verb}}{{/verb}}{{#trans}}, {{trans}}{{/trans}}{{#case}} ({{case}}){{/case}}</i></div>

<div class=brclass><br></div>

<div>  {{eng}}  </div>
<div class=brclass><br></div>

<div> {{native}} </div>

{{#comp}}
<div class=brclass><br></div>
<div style='font-size: 90%;'> <i>Comp: </i> {{comp}} ({{comp_constr}}) </div>
{{/comp}}

{{#sk}}
<div class=brclass><br></div>
<div style='font-size: 90%;'> <i>Sk:</i> {{sk}} </div>
{{/sk}}

<div style='font-size: 90%;'> {{#skroot}} <i>Sk:</I> {{/skroot}} {{skroot}} </div>

{{#comment}}
<div class=brclass><br></div>
<div class=smallclass> <i>{{comment}}</i></div>
{{/comment}}

{{#notes}}
<div class=brclass><br></div>
<div class=smallclass> <i>{{notes}}</i></div>
 {{/notes}}


<div class=brclass><br></div>
<div class=smallclass> <i></i></div>
 

{{#var}}
<div class=brclass><br></div>
<div class=smallclass> <i>Var:</i> {{var}}</div>
 {{/var}}

<div>{{audio}}</div>
<div class=brclass><br></div>
<div style='font-size: 70%; text-align: left;'>{{feedback}}</div>
<br>
