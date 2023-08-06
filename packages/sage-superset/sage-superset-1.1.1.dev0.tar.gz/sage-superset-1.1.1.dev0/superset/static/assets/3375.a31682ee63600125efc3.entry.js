"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[3375],{62276:(t,e,a)=>{a.d(e,{S:()=>o,M:()=>r});var n=a(11448),l=a(51995);const i=n.Z.RangePicker,o=(0,l.iK)(i)`
  border-radius: ${({theme:t})=>t.gridUnit}px;
`,r=n.Z},76697:(t,e,a)=>{a.d(e,{Z:()=>n});const n=a(19181).Z},82342:(t,e,a)=>{a.d(e,{Z:()=>d}),a(67294);var n=a(51995),l=a(11965),i=a(61988),o=a(9882),r=a(58593),s=a(49238),u=a(70163),c={name:"8wgs83",styles:"margin-bottom:0;position:relative"};const d=({name:t,label:e,description:a,validationErrors:d=[],renderTrigger:p=!1,rightNode:m,leftNode:h,onClick:Z,hovered:g=!1,tooltipOnClick:v=(()=>{}),warning:f,danger:y})=>{const{gridUnit:b,colors:C}=(0,n.Fg)();if(!e)return null;const w=(null==d?void 0:d.length)>0?"text-danger":"";return(0,l.tZ)("div",{className:"ControlHeader"},(0,l.tZ)("div",{className:"pull-left"},(0,l.tZ)(s.lX,{css:c},h&&(0,l.tZ)("span",null,h),(0,l.tZ)("span",{role:"button",tabIndex:0,onClick:Z,className:w,style:{cursor:Z?"pointer":""}},e)," ",f&&(0,l.tZ)("span",null,(0,l.tZ)(r.u,{id:"error-tooltip",placement:"top",title:f},(0,l.tZ)(u.Z.AlertSolid,{iconColor:C.alert.base,iconSize:"s"}))," "),y&&(0,l.tZ)("span",null,(0,l.tZ)(r.u,{id:"error-tooltip",placement:"top",title:y},(0,l.tZ)(u.Z.ErrorSolid,{iconColor:C.error.base,iconSize:"s"}))," "),(null==d?void 0:d.length)>0&&(0,l.tZ)("span",null,(0,l.tZ)(r.u,{id:"error-tooltip",placement:"top",title:null==d?void 0:d.join(" ")},(0,l.tZ)(u.Z.ErrorSolid,{iconColor:C.error.base,iconSize:"s"}))," "),g?(0,l.tZ)("span",{css:()=>l.iv`
          position: absolute;
          top: 50%;
          right: 0;
          padding-left: ${b}px;
          transform: translate(100%, -50%);
          white-space: nowrap;
        `},a&&(0,l.tZ)("span",null,(0,l.tZ)(o.V,{label:(0,i.t)("description"),tooltip:a,placement:"top",onClick:v})," "),p&&(0,l.tZ)("span",null,(0,l.tZ)(o.V,{label:(0,i.t)("bolt"),tooltip:(0,i.t)("Changing this control takes effect instantly"),placement:"top",icon:"bolt"})," ")):null)),m&&(0,l.tZ)("div",{className:"pull-right"},m),(0,l.tZ)("div",{className:"clearfix"}))}},73375:(t,e,a)=>{a.d(e,{Z:()=>St});var n=a(5872),l=a.n(n),i=a(67294),o=a(15926),r=a.n(o),s=a(31069),u=a(51995),c=a(61988),d=a(30381),p=a.n(d);const m=" : ",h=(t,e)=>t.replace("T00:00:00","")||(e?"-∞":"∞"),Z=t=>{const e=t.split(m);return 1===e.length?t:`${h(e[0],!0)} ≤ col < ${h(e[1])}`},g="previous calendar week",v="previous calendar month",f="previous calendar year",y=[{value:"Common",label:(0,c.t)("Last")},{value:"Calendar",label:(0,c.t)("Previous")},{value:"Custom",label:(0,c.t)("Custom")},{value:"Advanced",label:(0,c.t)("Advanced")},{value:"No filter",label:(0,c.t)("No filter")}],b=[{value:"Last day",label:(0,c.t)("last day")},{value:"Last week",label:(0,c.t)("last week")},{value:"Last month",label:(0,c.t)("last month")},{value:"Last quarter",label:(0,c.t)("last quarter")},{value:"Last year",label:(0,c.t)("last year")}],C=new Set(b.map((({value:t})=>t))),w=[{value:g,label:(0,c.t)("previous calendar week")},{value:v,label:(0,c.t)("previous calendar month")},{value:f,label:(0,c.t)("previous calendar year")}],E=new Set(w.map((({value:t})=>t))),D=[{value:"second",label:t=>(0,c.t)("Seconds %s",t)},{value:"minute",label:t=>(0,c.t)("Minutes %s",t)},{value:"hour",label:t=>(0,c.t)("Hours %s",t)},{value:"day",label:t=>(0,c.t)("Days %s",t)},{value:"week",label:t=>(0,c.t)("Weeks %s",t)},{value:"month",label:t=>(0,c.t)("Months %s",t)},{value:"quarter",label:t=>(0,c.t)("Quarters %s",t)},{value:"year",label:t=>(0,c.t)("Years %s",t)}],x=D.map((t=>({value:t.value,label:t.label((0,c.t)("Before"))}))),N=D.map((t=>({value:t.value,label:t.label((0,c.t)("After"))}))),S=[{value:"specific",label:(0,c.t)("Specific Date/Time")},{value:"relative",label:(0,c.t)("Relative Date/Time")},{value:"now",label:(0,c.t)("Now")},{value:"today",label:(0,c.t)("Midnight")}],T=S.slice(),$=new Set(["Last day","Last week","Last month","Last quarter","Last year"]),M=new Set([g,v,f]),A="YYYY-MM-DD[T]HH:mm:ss",V=p()().utc().startOf("day").subtract(7,"days").format(A),k=p()().utc().startOf("day").format(A),G=String.raw`\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?(?:(?:[+-]\d\d:\d\d)|Z)?`,R=String.raw`TODAY|NOW`,I=String.raw`[+-]?[1-9][0-9]*`,L=String.raw`YEAR|QUARTER|MONTH|WEEK|DAY|HOUR|MINUTE|SECOND`,X=RegExp(String.raw`^DATEADD\(DATETIME\("(${G}|${R})"\),\s(${I}),\s(${L})\)$`,"i"),Y=RegExp(String.raw`^${G}$|^${R}$`,"i"),U=["now","today"],z={sinceDatetime:V,sinceMode:"relative",sinceGrain:"day",sinceGrainValue:-7,untilDatetime:k,untilMode:"specific",untilGrain:"day",untilGrainValue:7,anchorMode:"now",anchorValue:"now"},F=["specific","today","now"],O=t=>"now"===t?p()().utc().startOf("second"):"today"===t?p()().utc().startOf("day"):p()(t),P=t=>O(t).format(A),q=t=>{const e=t.split(m);if(2===e.length){const[t,a]=e;if(Y.test(t)&&Y.test(a)){const e=U.includes(t)?t:"specific",n=U.includes(a)?a:"specific";return{customRange:{...z,sinceDatetime:t,untilDatetime:a,sinceMode:e,untilMode:n},matchedFlag:!0}}const n=t.match(X);if(n&&Y.test(a)&&t.includes(a)){const[t,e,l]=n.slice(1),i=U.includes(a)?a:"specific";return{customRange:{...z,sinceGrain:l,sinceGrainValue:parseInt(e,10),sinceDatetime:t,untilDatetime:t,sinceMode:"relative",untilMode:i},matchedFlag:!0}}const l=a.match(X);if(Y.test(t)&&l&&a.includes(t)){const[e,a,n]=[...l.slice(1)],i=U.includes(t)?t:"specific";return{customRange:{...z,untilGrain:n,untilGrainValue:parseInt(a,10),sinceDatetime:e,untilDatetime:e,untilMode:"relative",sinceMode:i},matchedFlag:!0}}if(n&&l){const[t,e,a]=[...n.slice(1)],[i,o,r]=[...l.slice(1)];if(t===i)return{customRange:{...z,sinceGrain:a,sinceGrainValue:parseInt(e,10),sinceDatetime:t,untilGrain:r,untilGrainValue:parseInt(o,10),untilDatetime:i,anchorValue:t,sinceMode:"relative",untilMode:"relative",anchorMode:"now"===t?"now":"specific"},matchedFlag:!0}}}return{customRange:z,matchedFlag:!1}},J=t=>{const{sinceDatetime:e,sinceMode:a,sinceGrain:n,sinceGrainValue:l,untilDatetime:i,untilMode:o,untilGrain:r,untilGrainValue:s,anchorValue:u}={...t};if(F.includes(a)&&F.includes(o))return`${"specific"===a?P(e):a} : ${"specific"===o?P(i):o}`;if(F.includes(a)&&"relative"===o){const t="specific"===a?P(e):a;return`${t} : DATEADD(DATETIME("${t}"), ${s}, ${r})`}if("relative"===a&&F.includes(o)){const t="specific"===o?P(i):o;return`DATEADD(DATETIME("${t}"), ${-Math.abs(l)}, ${n}) : ${t}`}return`DATEADD(DATETIME("${u}"), ${-Math.abs(l)}, ${n}) : DATEADD(DATETIME("${u}"), ${s}, ${r})`};var H=a(98286),K=a(35932),W=a(82342),j=a(37921),Q=a(76697),_=a(4715),B=a(70163),tt=a(24554),et=a(58593),at=a(69856),nt=a(12515),lt=a(27600),it=a(53350),ot=a(54076),rt=a(87183),st=a(11965);function ut(t){let e="Last week";return $.has(t.value)?e=t.value:t.onChange(e),(0,st.tZ)(i.Fragment,null,(0,st.tZ)("div",{className:"section-title"},(0,c.t)("Configure Time Range: Last...")),(0,st.tZ)(rt.Y.Group,{value:e,onChange:e=>t.onChange(e.target.value)},b.map((({value:t,label:e})=>(0,st.tZ)(rt.Y,{key:t,value:t,className:"vertical-radio"},e)))))}function ct({onChange:t,value:e}){return(0,i.useEffect)((()=>{M.has(e)||t(g)}),[t,e]),M.has(e)?(0,st.tZ)(i.Fragment,null,(0,st.tZ)("div",{className:"section-title"},(0,c.t)("Configure Time Range: Previous...")),(0,st.tZ)(rt.Y.Group,{value:e,onChange:e=>t(e.target.value)},w.map((({value:t,label:e})=>(0,st.tZ)(rt.Y,{key:t,value:t,className:"vertical-radio"},e))))):null}var dt=a(93754),pt=a.n(dt),mt=a(9875),ht=a(62276),Zt=a(9882);function gt(t){const{customRange:e,matchedFlag:a}=q(t.value);a||t.onChange(J(e));const{sinceDatetime:n,sinceMode:l,sinceGrain:i,sinceGrainValue:o,untilDatetime:r,untilMode:s,untilGrain:u,untilGrainValue:d,anchorValue:p,anchorMode:m}={...e};function h(a,n){t.onChange(J({...e,[a]:n}))}function Z(a,n){pt()(n)&&n>0&&t.onChange(J({...e,[a]:n}))}return(0,st.tZ)("div",null,(0,st.tZ)("div",{className:"section-title"},(0,c.t)("Configure custom time range")),(0,st.tZ)(_.X2,{gutter:24},(0,st.tZ)(_.JX,{span:12},(0,st.tZ)("div",{className:"control-label"},(0,c.t)("START (INCLUSIVE)")," ",(0,st.tZ)(Zt.V,{tooltip:(0,c.t)("Start date included in time range"),placement:"right"})),(0,st.tZ)(tt.ZP,{ariaLabel:(0,c.t)("START (INCLUSIVE)"),options:S,value:l,onChange:t=>h("sinceMode",t)}),"specific"===l&&(0,st.tZ)(_.X2,null,(0,st.tZ)(ht.M,{showTime:!0,defaultValue:O(n),onChange:t=>h("sinceDatetime",t.format(A)),allowClear:!1})),"relative"===l&&(0,st.tZ)(_.X2,{gutter:8},(0,st.tZ)(_.JX,{span:11},(0,st.tZ)(mt.Rn,{placeholder:(0,c.t)("Relative quantity"),value:Math.abs(o),min:1,defaultValue:1,onChange:t=>Z("sinceGrainValue",t||1),onStep:t=>Z("sinceGrainValue",t||1)})),(0,st.tZ)(_.JX,{span:13},(0,st.tZ)(tt.ZP,{ariaLabel:(0,c.t)("Relative period"),options:x,value:i,onChange:t=>h("sinceGrain",t)})))),(0,st.tZ)(_.JX,{span:12},(0,st.tZ)("div",{className:"control-label"},(0,c.t)("END (EXCLUSIVE)")," ",(0,st.tZ)(Zt.V,{tooltip:(0,c.t)("End date excluded from time range"),placement:"right"})),(0,st.tZ)(tt.ZP,{ariaLabel:(0,c.t)("END (EXCLUSIVE)"),options:T,value:s,onChange:t=>h("untilMode",t)}),"specific"===s&&(0,st.tZ)(_.X2,null,(0,st.tZ)(ht.M,{showTime:!0,defaultValue:O(r),onChange:t=>h("untilDatetime",t.format(A)),allowClear:!1})),"relative"===s&&(0,st.tZ)(_.X2,{gutter:8},(0,st.tZ)(_.JX,{span:11},(0,st.tZ)(mt.Rn,{placeholder:(0,c.t)("Relative quantity"),value:d,min:1,defaultValue:1,onChange:t=>Z("untilGrainValue",t||1),onStep:t=>Z("untilGrainValue",t||1)})),(0,st.tZ)(_.JX,{span:13},(0,st.tZ)(tt.ZP,{ariaLabel:(0,c.t)("Relative period"),options:N,value:u,onChange:t=>h("untilGrain",t)}))))),"relative"===l&&"relative"===s&&(0,st.tZ)("div",{className:"control-anchor-to"},(0,st.tZ)("div",{className:"control-label"},(0,c.t)("Anchor to")),(0,st.tZ)(_.X2,{align:"middle"},(0,st.tZ)(_.JX,null,(0,st.tZ)(rt.Y.Group,{onChange:function(a){const n=a.target.value;"now"===n?t.onChange(J({...e,anchorValue:"now",anchorMode:n})):t.onChange(J({...e,anchorValue:k,anchorMode:n}))},defaultValue:"now",value:m},(0,st.tZ)(rt.Y,{key:"now",value:"now"},(0,c.t)("NOW")),(0,st.tZ)(rt.Y,{key:"specific",value:"specific"},(0,c.t)("Date/Time")))),"now"!==m&&(0,st.tZ)(_.JX,null,(0,st.tZ)(ht.M,{showTime:!0,defaultValue:O(p),onChange:t=>h("anchorValue",t.format(A)),allowClear:!1,className:"control-anchor-to-datetime"})))))}const vt=(0,st.tZ)(i.Fragment,null,(0,st.tZ)("div",null,(0,st.tZ)("h3",null,"DATETIME"),(0,st.tZ)("p",null,(0,c.t)("Return to specific datetime.")),(0,st.tZ)("h4",null,(0,c.t)("Syntax")),(0,st.tZ)("pre",null,(0,st.tZ)("code",null,"datetime([string])")),(0,st.tZ)("h4",null,(0,c.t)("Example")),(0,st.tZ)("pre",null,(0,st.tZ)("code",null,'datetime("2020-03-01 12:00:00")\ndatetime("now")\ndatetime("last year")'))),(0,st.tZ)("div",null,(0,st.tZ)("h3",null,"DATEADD"),(0,st.tZ)("p",null,(0,c.t)("Moves the given set of dates by a specified interval.")),(0,st.tZ)("h4",null,(0,c.t)("Syntax")),(0,st.tZ)("pre",null,(0,st.tZ)("code",null,"dateadd([datetime], [integer], [dateunit])\ndateunit = (year | quarter | month | week | day | hour | minute | second)")),(0,st.tZ)("h4",null,(0,c.t)("Example")),(0,st.tZ)("pre",null,(0,st.tZ)("code",null,'dateadd(datetime("today"), -13, day)\ndateadd(datetime("2020-03-01"), 2, day)'))),(0,st.tZ)("div",null,(0,st.tZ)("h3",null,"DATETRUNC"),(0,st.tZ)("p",null,(0,c.t)("Truncates the specified date to the accuracy specified by the date unit.")),(0,st.tZ)("h4",null,(0,c.t)("Syntax")),(0,st.tZ)("pre",null,(0,st.tZ)("code",null,"datetrunc([datetime], [dateunit])\ndateunit = (year | quarter | month | week)")),(0,st.tZ)("h4",null,(0,c.t)("Example")),(0,st.tZ)("pre",null,(0,st.tZ)("code",null,'datetrunc(datetime("2020-03-01"), week)\ndatetrunc(datetime("2020-03-01"), month)'))),(0,st.tZ)("div",null,(0,st.tZ)("h3",null,"LASTDAY"),(0,st.tZ)("p",null,(0,c.t)("Get the last date by the date unit.")),(0,st.tZ)("h4",null,(0,c.t)("Syntax")),(0,st.tZ)("pre",null,(0,st.tZ)("code",null,"lastday([datetime], [dateunit])\ndateunit = (year | month | week)")),(0,st.tZ)("h4",null,(0,c.t)("Example")),(0,st.tZ)("pre",null,(0,st.tZ)("code",null,'lastday(datetime("today"), month)'))),(0,st.tZ)("div",null,(0,st.tZ)("h3",null,"HOLIDAY"),(0,st.tZ)("p",null,(0,c.t)("Get the specify date for the holiday")),(0,st.tZ)("h4",null,(0,c.t)("Syntax")),(0,st.tZ)("pre",null,(0,st.tZ)("code",null,"holiday([string])\nholiday([holiday string], [datetime])\nholiday([holiday string], [datetime], [country name])")),(0,st.tZ)("h4",null,(0,c.t)("Example")),(0,st.tZ)("pre",null,(0,st.tZ)("code",null,'holiday("new year")\nholiday("christmas", datetime("2019"))\nholiday("christmas", dateadd(datetime("2019"), 1, year))\nholiday("christmas", datetime("2 years ago"))\nholiday("Easter Monday", datetime("2019"), "UK")')))),ft=t=>{const e=(0,u.Fg)();return(0,st.tZ)(st.ms,null,(({css:a})=>(0,st.tZ)(et.u,l()({overlayClassName:a`
            .ant-tooltip-content {
              min-width: ${125*e.gridUnit}px;
              max-height: 410px;
              overflow-y: scroll;

              .ant-tooltip-inner {
                max-width: ${125*e.gridUnit}px;
                h3 {
                  font-size: ${e.typography.sizes.m}px;
                  font-weight: ${e.typography.weights.bold};
                }
                h4 {
                  font-size: ${e.typography.sizes.m}px;
                  font-weight: ${e.typography.weights.bold};
                }
                pre {
                  border: none;
                  text-align: left;
                  word-break: break-word;
                  font-size: ${e.typography.sizes.s}px;
                }
              }
            }
          `},t))))};function yt(t){return(0,st.tZ)(ft,l()({title:vt},t))}function bt(t){const e=l(t.value||""),[a,n]=e.split(m);function l(t){return t.includes(m)?t:t.startsWith("Last")?[t,""].join(m):t.startsWith("Next")?["",t].join(m):m}function o(e,l){"since"===e?t.onChange(`${l} : ${n}`):t.onChange(`${a} : ${l}`)}return e!==t.value&&t.onChange(l(t.value||"")),(0,st.tZ)(i.Fragment,null,(0,st.tZ)("div",{className:"section-title"},(0,c.t)("Configure Advanced Time Range "),(0,st.tZ)(yt,{placement:"rightBottom"},(0,st.tZ)("i",{className:"fa fa-info-circle text-muted"}))),(0,st.tZ)("div",{className:"control-label"},(0,c.t)("START (INCLUSIVE)")," ",(0,st.tZ)(Zt.V,{tooltip:(0,c.t)("Start date included in time range"),placement:"right"})),(0,st.tZ)(mt.II,{key:"since",value:a,onChange:t=>o("since",t.target.value)}),(0,st.tZ)("div",{className:"control-label"},(0,c.t)("END (EXCLUSIVE)")," ",(0,st.tZ)(Zt.V,{tooltip:(0,c.t)("End date excluded from time range"),placement:"right"})),(0,st.tZ)(mt.II,{key:"until",value:n,onChange:t=>o("until",t.target.value)}))}const Ct=async t=>{const e=`/api/v1/time_range/?q=${r().encode_uri(t)}`;try{var a,n,l,i;const t=await s.Z.get({endpoint:e}),o=`${(null==t||null==(a=t.json)||null==(n=a.result)?void 0:n.since)||""} : ${(null==t||null==(l=t.json)||null==(i=l.result)?void 0:i.until)||""}`;return{value:Z(o)}}catch(t){const e=await(0,H.O)(t);return{error:e.message||e.error}}},wt=(0,u.iK)(Q.Z)``,Et=(0,u.iK)(tt.ZP)`
  width: 272px;
`,Dt=u.iK.div`
  .ant-row {
    margin-top: 8px;
  }

  .ant-input-number {
    width: 100%;
  }

  .ant-picker {
    padding: 4px 17px 4px;
    border-radius: 4px;
    width: 100%;
  }

  .ant-divider-horizontal {
    margin: 16px 0;
  }

  .control-label {
    font-size: 11px;
    font-weight: 500;
    color: #b2b2b2;
    line-height: 16px;
    text-transform: uppercase;
    margin: 8px 0;
  }

  .vertical-radio {
    display: block;
    height: 40px;
    line-height: 40px;
  }

  .section-title {
    font-style: normal;
    font-weight: 500;
    font-size: 15px;
    line-height: 24px;
    margin-bottom: 8px;
  }

  .control-anchor-to {
    margin-top: 16px;
  }

  .control-anchor-to-datetime {
    width: 217px;
  }

  .footer {
    text-align: right;
  }
`,xt=u.iK.span`
  span {
    margin-right: ${({theme:t})=>2*t.gridUnit}px;
    vertical-align: middle;
  }
  .text {
    vertical-align: middle;
  }
  .error {
    color: ${({theme:t})=>t.colors.error.base};
  }
`,Nt=(0,it.Q)("date-filter-control");function St(t){const{value:e=at.X5,onChange:a,type:n,onOpenPopover:o=ot.EI,onClosePopover:r=ot.EI}=t,[s,d]=(0,i.useState)(e),[p,m]=(0,i.useState)(!1),h=(0,i.useMemo)((()=>{return t=e,C.has(t)?"Common":E.has(t)?"Calendar":"No filter"===t?"No filter":q(t).matchedFlag?"Custom":"Advanced";var t}),[e]),[Z,g]=(0,i.useState)(h),[v,f]=(0,i.useState)(e),[b,w]=(0,i.useState)(e),[D,x]=(0,i.useState)(!1),[N,S]=(0,i.useState)(e),[T,$]=(0,i.useState)(e);function M(){w(e),g(h),m(!1)}(0,i.useEffect)((()=>{Ct(e).then((({value:t,error:a})=>{a?(S(a||""),x(!1),$(e||"")):("Common"===h||"Calendar"===h||"No filter"===h?(d(e),$("error"===n?(0,c.t)("Default value is required"):t||"")):(d(t||""),$(e||"")),x(!0)),f(e)}))}),[e]),(0,nt.bX)((()=>{v!==b&&Ct(b).then((({value:t,error:e})=>{e?(S(e||""),x(!1)):(S(t||""),x(!0)),f(b)}))}),lt.M$,[b]);const A=(0,u.Fg)(),V=(0,st.tZ)(Dt,null,(0,st.tZ)("div",{className:"control-label"},(0,c.t)("RANGE TYPE")),(0,st.tZ)(Et,{ariaLabel:(0,c.t)("RANGE TYPE"),options:y,value:Z,onChange:function(t){"No filter"===t&&w("No filter"),g(t)}}),"No filter"!==Z&&(0,st.tZ)(_.iz,null),"Common"===Z&&(0,st.tZ)(ut,{value:b,onChange:w}),"Calendar"===Z&&(0,st.tZ)(ct,{value:b,onChange:w}),"Advanced"===Z&&(0,st.tZ)(bt,{value:b,onChange:w}),"Custom"===Z&&(0,st.tZ)(gt,{value:b,onChange:w}),"No filter"===Z&&(0,st.tZ)("div",null),(0,st.tZ)(_.iz,null),(0,st.tZ)("div",null,(0,st.tZ)("div",{className:"section-title"},(0,c.t)("Actual time range")),D&&(0,st.tZ)("div",null,N),!D&&(0,st.tZ)(xt,{className:"warning"},(0,st.tZ)(B.Z.ErrorSolidSmall,{iconColor:A.colors.error.base}),(0,st.tZ)("span",{className:"text error"},N))),(0,st.tZ)(_.iz,null),(0,st.tZ)("div",{className:"footer"},(0,st.tZ)(K.Z,{buttonStyle:"secondary",cta:!0,key:"cancel",onClick:M},(0,c.t)("CANCEL")),(0,st.tZ)(K.Z,l()({buttonStyle:"primary",cta:!0,disabled:!D,key:"apply",onClick:function(){a(b),m(!1)}},Nt("apply-button")),(0,c.t)("APPLY")))),k=(0,st.tZ)(xt,null,(0,st.tZ)(B.Z.EditAlt,{iconColor:A.colors.grayscale.base}),(0,st.tZ)("span",{className:"text"},(0,c.t)("Edit time range")));return(0,st.tZ)(i.Fragment,null,(0,st.tZ)(W.Z,t),(0,st.tZ)(wt,{placement:"right",trigger:"click",content:V,title:k,defaultVisible:p,visible:p,onVisibleChange:()=>{p?(M(),r()):(w(e),g(h),m(!0),o())},overlayStyle:{width:"600px"}},(0,st.tZ)(et.u,{placement:"top",title:T},(0,st.tZ)(j.Z,{className:"pointer"},s))))}},53350:(t,e,a)=>{a.d(e,{Q:()=>n});const n=(t,e=!1)=>(a,n=!1)=>{const l=n||e;if(!a&&t)return l?t:{"data-test":t};if(a&&!t)return l?a:{"data-test":a};if(!a&&!t)return console.warn('testWithId function has missed "prefix" and "id" params'),l?"":{"data-test":""};const i=`${t}__${a}`;return l?i:{"data-test":i}}}}]);