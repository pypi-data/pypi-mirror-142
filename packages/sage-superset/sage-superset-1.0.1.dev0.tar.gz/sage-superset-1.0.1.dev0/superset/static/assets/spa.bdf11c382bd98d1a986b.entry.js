(()=>{var e,t,a,i,n,r,d,o,l={43063:(e,t,a)=>{var i=a(34963),n=a(80760),r=a(67206),d=a(1469),o=a(94885);e.exports=function(e,t){return(d(e)?i:n)(e,o(r(t,3)))}},79789:(e,t,a)=>{"use strict";a.d(t,{Z:()=>s});var i=a(67294),n=a(61988),r=a(51995),d=a(70163),o=a(58593),l=a(11965);const s=function({certifiedBy:e,details:t,size:a="l"}){return(0,l.tZ)(o.u,{id:"certified-details-tooltip",title:(0,l.tZ)(i.Fragment,null,e&&(0,l.tZ)("div",null,(0,l.tZ)("strong",null,(0,n.t)("Certified by %s",e))),(0,l.tZ)("div",null,t))},(0,l.tZ)(d.Z.Certified,{iconColor:r.K6.colors.primary.base,iconSize:a}))}},19259:(e,t,a)=>{"use strict";a.d(t,{Z:()=>d});var i=a(67294),n=a(17198),r=a(11965);function d({title:e,description:t,onConfirm:a,children:d}){const[o,l]=(0,i.useState)(!1),[s,c]=(0,i.useState)([]),u=()=>{l(!1),c([])};return(0,r.tZ)(i.Fragment,null,d&&d(((...e)=>{e.forEach((e=>{e&&("function"==typeof e.persist&&e.persist(),"function"==typeof e.preventDefault&&e.preventDefault(),"function"==typeof e.stopPropagation&&e.stopPropagation())})),l(!0),c(e)})),(0,r.tZ)(n.Z,{description:t,onConfirm:()=>{a(...s),u()},onHide:u,open:o,title:e}))}},17198:(e,t,a)=>{"use strict";a.d(t,{Z:()=>b});var i=a(51995),n=a(61988),r=a(67294),d=a(9875),o=a(74069),l=a(49238),s=a(11965);const c=i.iK.div`
  padding-top: 8px;
  width: 50%;
  label {
    color: ${({theme:e})=>e.colors.grayscale.base};
    text-transform: uppercase;
  }
`,u=i.iK.div`
  line-height: 40px;
  padding-top: 16px;
`;function b({description:e,onConfirm:t,onHide:a,open:i,title:b}){const[f,h]=(0,r.useState)(!0),[m,p]=(0,r.useState)(""),g=()=>{p(""),t()};return(0,s.tZ)(o.Z,{disablePrimaryButton:f,onHide:()=>{p(""),a()},onHandledPrimaryAction:g,primaryButtonName:(0,n.t)("delete"),primaryButtonType:"danger",show:i,title:b},(0,s.tZ)(u,null,e),(0,s.tZ)(c,null,(0,s.tZ)(l.lX,{htmlFor:"delete"},(0,n.t)('Type "%s" to confirm',(0,n.t)("DELETE"))),(0,s.tZ)(d.II,{type:"text",id:"delete",autoComplete:"off",value:m,onChange:e=>{var t;const a=null!=(t=e.target.value)?t:"";h(a.toUpperCase()!==(0,n.t)("DELETE")),p(a)},onPressEnter:()=>{f||g()}})))}},36674:(e,t,a)=>{"use strict";a.d(t,{Z:()=>u});var i=a(67294),n=a(51995),r=a(61988),d=a(58593),o=a(33626),l=a(70163),s=a(11965);const c=n.iK.a`
  font-size: ${({theme:e})=>e.typography.sizes.xl}px;
  display: flex;
  padding: 0 0 0 0.5em;
`,u=({itemId:e,isStarred:t,showTooltip:a,saveFaveStar:n,fetchFaveStar:u})=>{(0,o.J)((()=>{u&&u(e)}));const b=(0,i.useCallback)((a=>{a.preventDefault(),n(e,!!t)}),[t,e,n]),f=(0,s.tZ)(c,{href:"#",onClick:b,className:"fave-unfave-icon",role:"button"},t?(0,s.tZ)(l.Z.FavoriteSelected,{iconSize:"xxl"}):(0,s.tZ)(l.Z.FavoriteUnselected,{iconSize:"xxl"}));return a?(0,s.tZ)(d.u,{id:"fave-unfave-tooltip",title:(0,r.t)("Click to favorite/unfavorite")},f):f}},55467:(e,t,a)=>{"use strict";a.d(t,{Z:()=>k});var i=a(11965),n=a(67294),r=a(51995),d=a(4715),o=a(58593),l=a(5872),s=a.n(l),c=a(68492);const u=r.iK.div`
  background-image: url(${({src:e})=>e});
  background-size: cover;
  background-position: center ${({position:e})=>e};
  display: inline-block;
  height: calc(100% - 1px);
  width: calc(100% - 2px);
  margin: 1px 1px 0 1px;
`;function b({src:e,fallback:t,isLoading:a,position:r,...d}){const[o,l]=(0,n.useState)(t);return(0,n.useEffect)((()=>(e&&fetch(e).then((e=>e.blob())).then((e=>{if(/image/.test(e.type)){const t=URL.createObjectURL(e);l(t)}})).catch((e=>{c.Z.error(e),l(t)})),()=>{l(t)})),[e,t]),(0,i.tZ)(u,s()({src:a?t:o},d,{position:r}))}var f=a(79789);const h=r.iK.div`
  width: 64px;
  display: flex;
  justify-content: space-between;
`,m=(0,r.iK)(d.Ak)`
  border: 1px solid #d9dbe4;
  border-radius: ${({theme:e})=>e.gridUnit}px;
  overflow: hidden;

  .ant-card-body {
    padding: ${({theme:e})=>4*e.gridUnit}px
      ${({theme:e})=>2*e.gridUnit}px;
  }
  .ant-card-meta-detail > div:not(:last-child) {
    margin-bottom: 0;
  }
  .gradient-container {
    position: relative;
    height: 100%;
  }
  &:hover {
    box-shadow: 8px 8px 28px 0px rgba(0, 0, 0, 0.24);
    transition: box-shadow ${({theme:e})=>e.transitionTiming}s ease-in-out;

    .gradient-container:after {
      content: '';
      position: absolute;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      display: inline-block;
      background: linear-gradient(
        180deg,
        rgba(0, 0, 0, 0) 47.83%,
        rgba(0, 0, 0, 0.219135) 79.64%,
        rgba(0, 0, 0, 0.5) 100%
      );

      transition: background ${({theme:e})=>e.transitionTiming}s
        ease-in-out;
    }

    .cover-footer {
      transform: translateY(0);
    }
  }
`,p=r.iK.div`
  height: 264px;
  border-bottom: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
  overflow: hidden;

  .cover-footer {
    transform: translateY(${({theme:e})=>9*e.gridUnit}px);
    transition: ${({theme:e})=>e.transitionTiming}s ease-out;
  }
`,g=r.iK.div`
  display: flex;
  justify-content: flex-start;
  flex-direction: row;

  .card-actions {
    margin-left: auto;
    align-self: flex-end;
    padding-left: ${({theme:e})=>e.gridUnit}px;
    span[role='img'] {
      display: flex;
      align-items: center;
    }
  }
`,v=r.iK.span`
  overflow: hidden;
  text-overflow: ellipsis;
  & a {
    color: ${({theme:e})=>e.colors.grayscale.dark1} !important;
  }
`,Z=r.iK.span`
  position: absolute;
  right: -1px;
  bottom: ${({theme:e})=>e.gridUnit}px;
`,y=r.iK.div`
  display: flex;
  flex-wrap: nowrap;
  position: relative;
  top: -${({theme:e})=>9*e.gridUnit}px;
  padding: 0 8px;
`,_=r.iK.div`
  flex: 1;
  overflow: hidden;
`,w=r.iK.div`
  align-self: flex-end;
  margin-left: auto;
  max-width: 200px;
  overflow: hidden;
  text-overflow: ellipsis;
`,x=(0,r.iK)(d.Od)`
  h3 {
    margin: ${({theme:e})=>e.gridUnit}px 0;
  }

  ul {
    margin-bottom: 0;
  }
`,C={rows:1,width:150},S=({to:e,children:t})=>(0,i.tZ)("a",{href:e},t);function E({title:e,url:t,linkComponent:a,titleRight:l,imgURL:s,imgFallbackURL:c,description:u,coverLeft:h,coverRight:E,actions:k,avatar:T,loading:I,imgPosition:$="top",cover:N,certifiedBy:D,certificationDetails:F}){const R=t&&a?a:S,L=(0,r.Fg)();return(0,i.tZ)(m,{cover:N||(0,i.tZ)(p,null,(0,i.tZ)(R,{to:t},(0,i.tZ)("div",{className:"gradient-container"},(0,i.tZ)(b,{src:s||"",fallback:c||"",isLoading:I,position:$}))),(0,i.tZ)(y,{className:"cover-footer"},!I&&h&&(0,i.tZ)(_,null,h),!I&&E&&(0,i.tZ)(w,null,E)))},I&&(0,i.tZ)(d.Ak.Meta,{title:(0,i.tZ)(n.Fragment,null,(0,i.tZ)(g,null,(0,i.tZ)(d.Od.Input,{active:!0,size:"small",css:(0,i.iv)({width:Math.trunc(62.5*L.gridUnit)},"","")}),(0,i.tZ)("div",{className:"card-actions"},(0,i.tZ)(d.Od.Button,{active:!0,shape:"circle"})," ",(0,i.tZ)(d.Od.Button,{active:!0,css:(0,i.iv)({width:10*L.gridUnit},"","")})))),description:(0,i.tZ)(x,{round:!0,active:!0,title:!1,paragraph:C})}),!I&&(0,i.tZ)(d.Ak.Meta,{title:(0,i.tZ)(g,null,(0,i.tZ)(o.u,{title:e},(0,i.tZ)(v,null,(0,i.tZ)(R,{to:t},D&&(0,i.tZ)(n.Fragment,null,(0,i.tZ)(f.Z,{certifiedBy:D,details:F})," "),e))),l&&(0,i.tZ)(Z,null,l),(0,i.tZ)("div",{className:"card-actions"},k)),description:u,avatar:T||null}))}E.Actions=h;const k=E},83673:(e,t,a)=>{"use strict";a.d(t,{Z:()=>Z});var i=a(67294),n=a(74069),r=a(9875),d=a(35932),o=a(4715),l=a(15926),s=a.n(l),c=a(51995),u=a(61988),b=a(31069),f=a(98286),h=a(14114),m=a(11965);const p=o.qz.Item,g=(0,c.iK)(o.qz.Item)`
  margin-bottom: 0;
`,v=c.iK.span`
  margin-bottom: 0;
`,Z=(0,h.Z)((function({slice:e,onHide:t,onSave:a,show:l,addSuccessToast:c}){const[h,Z]=(0,i.useState)(!1),[y]=o.qz.useForm(),[_,w]=(0,i.useState)(e.slice_name||""),[x,C]=(0,i.useState)(null);function S({error:e,statusText:t,message:a}){let i=e||t||(0,u.t)("An error has occurred");"Forbidden"===a&&(i=(0,u.t)("You do not have permission to edit this chart")),n.Z.error({title:"Error",content:i,okButtonProps:{danger:!0,className:"btn-danger"}})}const E=(0,i.useCallback)((async function(){try{const t=(await b.Z.get({endpoint:`/api/v1/chart/${e.slice_id}`})).json.result;C(t.owners.map((e=>({value:e.id,label:`${e.first_name} ${e.last_name}`}))))}catch(e){S(await(0,f.O)(e))}}),[e.slice_id]),k=(0,i.useMemo)((()=>(e="",t,a)=>{const i=s().encode({filter:e,page:t,page_size:a});return b.Z.get({endpoint:`/api/v1/chart/related/owners?q=${i}`}).then((e=>({data:e.json.result.map((e=>({value:e.value,label:e.text}))),totalCount:e.json.count})))}),[]),T=(0,u.t)("Owners");return(0,i.useEffect)((()=>{E()}),[E]),(0,i.useEffect)((()=>{w(e.slice_name||"")}),[e.slice_name]),(0,m.tZ)(n.Z,{show:l,onHide:t,title:"Edit Chart Properties",footer:(0,m.tZ)(i.Fragment,null,(0,m.tZ)(d.Z,{htmlType:"button",buttonSize:"small",onClick:t,cta:!0},(0,u.t)("Cancel")),(0,m.tZ)(d.Z,{htmlType:"submit",buttonSize:"small",buttonStyle:"primary",onClick:y.submit,disabled:h||!_,cta:!0},(0,u.t)("Save"))),responsive:!0,wrapProps:{"data-test":"properties-edit-modal"}},(0,m.tZ)(o.qz,{form:y,onFinish:async i=>{Z(!0);const{certified_by:n,certification_details:r,description:d,cache_timeout:o}=i,l={slice_name:_||null,description:d||null,cache_timeout:o||null,certified_by:n||null,certification_details:n&&r?r:null};x&&(l.owners=x.map((e=>e.value)));try{const i=await b.Z.put({endpoint:`/api/v1/chart/${e.slice_id}`,headers:{"Content-Type":"application/json"},body:JSON.stringify(l)}),n={...l,...i.json.result,id:e.slice_id};a(n),c((0,u.t)("Chart properties updated")),t()}catch(e){S(await(0,f.O)(e))}Z(!1)},layout:"vertical",initialValues:{name:e.slice_name||"",description:e.description||"",cache_timeout:null!=e.cache_timeout?e.cache_timeout:"",certified_by:e.certified_by||"",certification_details:e.certified_by&&e.certification_details?e.certification_details:""}},(0,m.tZ)(o.X2,{gutter:16},(0,m.tZ)(o.JX,{xs:24,md:12},(0,m.tZ)("h3",null,(0,u.t)("Basic information")),(0,m.tZ)(p,{label:(0,u.t)("Name"),required:!0},(0,m.tZ)(r.II,{"aria-label":(0,u.t)("Name"),name:"name",type:"text",value:_,onChange:e=>{var t;return w(null!=(t=e.target.value)?t:"")}})),(0,m.tZ)(p,null,(0,m.tZ)(g,{label:(0,u.t)("Description"),name:"description"},(0,m.tZ)(r.Kx,{rows:3,style:{maxWidth:"100%"}})),(0,m.tZ)(v,{className:"help-block"},(0,u.t)("The description can be displayed as widget headers in the dashboard view. Supports markdown."))),(0,m.tZ)("h3",null,(0,u.t)("Certification")),(0,m.tZ)(p,null,(0,m.tZ)(g,{label:(0,u.t)("Certified by"),name:"certified_by"},(0,m.tZ)(r.II,{"aria-label":(0,u.t)("Certified by")})),(0,m.tZ)(v,{className:"help-block"},(0,u.t)("Person or group that has certified this chart."))),(0,m.tZ)(p,null,(0,m.tZ)(g,{label:(0,u.t)("Certification details"),name:"certification_details"},(0,m.tZ)(r.II,{"aria-label":(0,u.t)("Certification details")})),(0,m.tZ)(v,{className:"help-block"},(0,u.t)("Any additional detail to show in the certification tooltip.")))),(0,m.tZ)(o.JX,{xs:24,md:12},(0,m.tZ)("h3",null,(0,u.t)("Configuration")),(0,m.tZ)(p,null,(0,m.tZ)(g,{label:(0,u.t)("Cache timeout"),name:"cache_timeout"},(0,m.tZ)(r.II,{"aria-label":"Cache timeout"})),(0,m.tZ)(v,{className:"help-block"},(0,u.t)("Duration (in seconds) of the caching timeout for this chart. Note this defaults to the dataset's timeout if undefined."))),(0,m.tZ)("h3",{style:{marginTop:"1em"}},(0,u.t)("Access")),(0,m.tZ)(p,{label:T},(0,m.tZ)(o.Ph,{ariaLabel:T,mode:"multiple",name:"owners",value:x||[],onChange:C,options:k,disabled:!x,allowClear:!0}),(0,m.tZ)(v,{className:"help-block"},(0,u.t)("A list of users who can alter the chart. Searchable by name or username.")))))))}))},33626:(e,t,a)=>{"use strict";a.d(t,{J:()=>n});var i=a(67294);const n=e=>{(0,i.useEffect)(e,[])}},32228:(e,t,a)=>{"use strict";a.d(t,{Z:()=>l});var i=a(89816),n=a(15926),r=a.n(n),d=a(14670),o=a.n(d);function l(e,t,a,n=200){const d=o().generate(),l=`/api/v1/${e}/export/?q=${r().encode(t)}&token=${d}`,s=document.createElement("iframe");s.style.display="none",s.src=l,document.body.appendChild(s);const c=window.setInterval((()=>{"done"===(0,i.Z)()[d]&&(window.clearInterval(c),document.body.removeChild(s),a())}),n)}},61337:(e,t,a)=>{"use strict";var i;function n(e,t){return d(e,t)}function r(e,t){o(e,t)}function d(e,t){try{const a=localStorage.getItem(e);return null===a?t:JSON.parse(a)}catch{return t}}function o(e,t){try{localStorage.setItem(e,JSON.stringify(t))}catch{}}a.d(t,{dR:()=>i,rV:()=>n,LS:()=>r,OH:()=>d,I_:()=>o}),function(e){e.filter_box_transition_snoozed_at="filter_box_transition_snoozed_at",e.chart_split_sizes="chart_split_sizes",e.controls_width="controls_width",e.datasource_width="datasource_width",e.is_datapanel_open="is_datapanel_open",e.homepage_chart_filter="homepage_chart_filter",e.homepage_dashboard_filter="homepage_dashboard_filter",e.homepage_collapse_state="homepage_collapse_state",e.homepage_activity_filter="homepage_activity_filter",e.sqllab__is_autocomplete_enabled="sqllab__is_autocomplete_enabled",e.explore__data_table_time_formatted_columns="explore__data_table_time_formatted_columns"}(i||(i={}))},34024:(e,t,a)=>{"use strict";a.d(t,{Z:()=>v});var i=a(67294),n=a(51995),r=a(61988),d=a(91877),o=a(93185),l=a(19259),s=a(70163),c=a(55467),u=a(37921),b=a(4715),f=a(83862),h=a(36674),m=a(34581),p=a(40768),g=a(11965);function v({chart:e,hasPerm:t,openChartEditModal:a,bulkSelectEnabled:v,addDangerToast:Z,addSuccessToast:y,refreshData:_,loading:w,showThumbnails:x,saveFavoriteStatus:C,favoriteStatus:S,chartFilter:E,userId:k,handleBulkChartExport:T}){const I=t("can_write"),$=t("can_write"),N=t("can_export")&&(0,d.cr)(o.T.VERSIONED_EXPORT),D=(0,n.Fg)(),F=(0,g.tZ)(f.v,null,$&&(0,g.tZ)(f.v.Item,null,(0,g.tZ)(l.Z,{title:(0,r.t)("Please confirm"),description:(0,g.tZ)(i.Fragment,null,(0,r.t)("Are you sure you want to delete")," ",(0,g.tZ)("b",null,e.slice_name),"?"),onConfirm:()=>(0,p.Gm)(e,y,Z,_,E,k)},(e=>(0,g.tZ)("div",{role:"button",tabIndex:0,className:"action-button",onClick:e},(0,g.tZ)(s.Z.Trash,{iconSize:"l"})," ",(0,r.t)("Delete"))))),N&&(0,g.tZ)(f.v.Item,null,(0,g.tZ)("div",{role:"button",tabIndex:0,onClick:()=>T([e])},(0,g.tZ)(s.Z.Share,{iconSize:"l"})," ",(0,r.t)("Export"))),I&&(0,g.tZ)(f.v.Item,null,(0,g.tZ)("div",{role:"button",tabIndex:0,onClick:()=>a(e)},(0,g.tZ)(s.Z.EditAlt,{iconSize:"l"})," ",(0,r.t)("Edit"))));return(0,g.tZ)(p.ZB,{onClick:()=>{!v&&e.url&&(window.location.href=e.url)}},(0,g.tZ)(c.Z,{loading:w,title:e.slice_name,certifiedBy:e.certified_by,certificationDetails:e.certification_details,cover:(0,d.cr)(o.T.THUMBNAILS)&&x?null:(0,g.tZ)(i.Fragment,null),url:v?void 0:e.url,imgURL:e.thumbnail_url||"",imgFallbackURL:"/static/assets/images/chart-card-fallback.svg",description:(0,r.t)("Modified %s",e.changed_on_delta_humanized),coverLeft:(0,g.tZ)(m.Z,{users:e.owners||[]}),coverRight:(0,g.tZ)(u.Z,{type:"secondary"},e.datasource_name_text),actions:(0,g.tZ)(c.Z.Actions,{onClick:e=>{e.stopPropagation(),e.preventDefault()}},(0,g.tZ)(h.Z,{itemId:e.id,saveFaveStar:C,isStarred:S}),(0,g.tZ)(b.Gj,{overlay:F},(0,g.tZ)(s.Z.MoreVert,{iconColor:D.colors.grayscale.base})))}))}},99415:(e,t,a)=>{"use strict";a.d(t,{Z:()=>y});var i=a(67294),n=a(5977),r=a(73727),d=a(51995),o=a(61988),l=a(40768),s=a(91877),c=a(93185),u=a(4715),b=a(83862),f=a(19259),h=a(55467),m=a(70163),p=a(37921),g=a(34581),v=a(36674),Z=a(11965);const y=function({dashboard:e,hasPerm:t,bulkSelectEnabled:a,dashboardFilter:y,refreshData:_,userId:w,addDangerToast:x,addSuccessToast:C,openDashboardEditModal:S,favoriteStatus:E,saveFavoriteStatus:k,showThumbnails:T,handleBulkDashboardExport:I}){const $=(0,n.k6)(),N=t("can_write"),D=t("can_write"),F=t("can_export"),R=(0,d.Fg)(),L=(0,Z.tZ)(b.v,null,N&&S&&(0,Z.tZ)(b.v.Item,null,(0,Z.tZ)("div",{role:"button",tabIndex:0,className:"action-button",onClick:()=>S&&S(e)},(0,Z.tZ)(m.Z.EditAlt,{iconSize:"l"})," ",(0,o.t)("Edit"))),F&&(0,Z.tZ)(b.v.Item,null,(0,Z.tZ)("div",{role:"button",tabIndex:0,onClick:()=>I([e]),className:"action-button"},(0,Z.tZ)(m.Z.Share,{iconSize:"l"})," ",(0,o.t)("Export"))),D&&(0,Z.tZ)(b.v.Item,null,(0,Z.tZ)(f.Z,{title:(0,o.t)("Please confirm"),description:(0,Z.tZ)(i.Fragment,null,(0,o.t)("Are you sure you want to delete")," ",(0,Z.tZ)("b",null,e.dashboard_title),"?"),onConfirm:()=>(0,l.Iu)(e,_,C,x,y,w)},(e=>(0,Z.tZ)("div",{role:"button",tabIndex:0,className:"action-button",onClick:e},(0,Z.tZ)(m.Z.Trash,{iconSize:"l"})," ",(0,o.t)("Delete"))))));return(0,Z.tZ)(l.ZB,{onClick:()=>{a||$.push(e.url)}},(0,Z.tZ)(h.Z,{loading:e.loading||!1,title:e.dashboard_title,certifiedBy:e.certified_by,certificationDetails:e.certification_details,titleRight:(0,Z.tZ)(p.Z,null,e.published?(0,o.t)("published"):(0,o.t)("draft")),cover:(0,s.cr)(c.T.THUMBNAILS)&&T?null:(0,Z.tZ)(i.Fragment,null),url:a?void 0:e.url,linkComponent:r.rU,imgURL:e.thumbnail_url,imgFallbackURL:"/static/assets/images/dashboard-card-fallback.svg",description:(0,o.t)("Modified %s",e.changed_on_delta_humanized),coverLeft:(0,Z.tZ)(g.Z,{users:e.owners||[]}),actions:(0,Z.tZ)(h.Z.Actions,{onClick:e=>{e.stopPropagation(),e.preventDefault()}},(0,Z.tZ)(v.Z,{itemId:e.id,saveFaveStar:k,isStarred:E}),(0,Z.tZ)(u.Gj,{overlay:L},(0,Z.tZ)(m.Z.MoreVert,{iconColor:R.colors.grayscale.base})))}))}},12:(e,t,a)=>{"use strict";var i,n;a.d(t,{s:()=>i,J:()=>n}),function(e){e.FAVORITE="Favorite",e.MINE="Mine",e.EXAMPLES="Examples"}(i||(i={})),function(e){e.id="id",e.changed_on="changed_on",e.database="database",e.database_name="database.database_name",e.schema="schema",e.sql="sql",e.executed_sql="exceuted_sql",e.sql_tables="sql_tables",e.status="status",e.tab_name="tab_name",e.user="user",e.user_first_name="user.first_name",e.start_time="start_time",e.end_time="end_time",e.rows="rows",e.tmp_table_name="tmp_table_name",e.tracking_url="tracking_url"}(n||(n={}))},20755:(e,t,a)=>{"use strict";a.d(t,{Z:()=>p});var i=a(23279),n=a.n(i),r=a(67294),d=a(5977),o=a(73727),l=a(51995),s=a(94184),c=a.n(s),u=a(4715),b=a(83862),f=a(35932),h=a(11965);const m=l.iK.div`
  margin-bottom: ${({theme:e})=>4*e.gridUnit}px;
  .header {
    font-weight: ${({theme:e})=>e.typography.weights.bold};
    margin-right: ${({theme:e})=>3*e.gridUnit}px;
    text-align: left;
    font-size: 18px;
    padding: ${({theme:e})=>3*e.gridUnit}px;
    display: inline-block;
    line-height: ${({theme:e})=>9*e.gridUnit}px;
  }
  .nav-right {
    display: flex;
    align-items: center;
    padding: 14px 0;
    margin-right: ${({theme:e})=>3*e.gridUnit}px;
    float: right;
    position: absolute;
    right: 0;
  }
  .nav-right-collapse {
    display: flex;
    align-items: center;
    padding: 14px 0;
    margin-right: 0;
    float: left;
    padding-left: 10px;
  }
  .menu {
    background-color: white;
    .ant-menu-horizontal {
      line-height: inherit;
      .ant-menu-item {
        &:hover {
          border-bottom: none;
        }
      }
    }
    .ant-menu {
      padding: ${({theme:e})=>4*e.gridUnit}px 0px;
    }
  }

  .ant-menu-horizontal:not(.ant-menu-dark) > .ant-menu-item {
    margin: 0 ${({theme:e})=>e.gridUnit+1}px;
  }

  .menu .ant-menu-item {
    li {
      a,
      div {
        font-size: ${({theme:e})=>e.typography.sizes.s}px;
        color: ${({theme:e})=>e.colors.secondary.dark1};

        a {
          margin: 0;
          padding: ${({theme:e})=>4*e.gridUnit}px;
          line-height: ${({theme:e})=>5*e.gridUnit}px;
        }
      }

      &.no-router a {
        padding: ${({theme:e})=>2*e.gridUnit}px
          ${({theme:e})=>4*e.gridUnit}px;
      }
    }
    li.active > a,
    li.active > div,
    li > a:hover,
    li > a:focus,
    li > div:hover {
      background: ${({theme:e})=>e.colors.secondary.light4};
      border-bottom: none;
      border-radius: ${({theme:e})=>e.borderRadius}px;
      margin-bottom: ${({theme:e})=>2*e.gridUnit}px;
      text-decoration: none;
    }
  }

  .btn-link {
    padding: 10px 0;
  }
  .ant-menu-horizontal {
    border: none;
  }
  @media (max-width: 767px) {
    .header,
    .nav-right {
      position: relative;
      margin-left: ${({theme:e})=>2*e.gridUnit}px;
    }
  }
`,p=e=>{var t,a;const[i,l]=(0,r.useState)("horizontal"),[s,p]=(0,r.useState)("nav-right");let g=!0;try{(0,d.k6)()}catch(e){g=!1}return(0,r.useEffect)((()=>{function t(){window.innerWidth<=767?l("inline"):l("horizontal"),e.buttons&&e.buttons.length>=3&&window.innerWidth>=795?p("nav-right"):e.buttons&&e.buttons.length>=3&&window.innerWidth<=795&&p("nav-right-collapse")}t();const a=n()(t,10);return window.addEventListener("resize",a),()=>window.removeEventListener("resize",a)}),[e.buttons]),(0,h.tZ)(m,null,(0,h.tZ)(u.X2,{className:"menu",role:"navigation"},e.name&&(0,h.tZ)("div",{className:"header"},e.name),(0,h.tZ)(b.v,{mode:i,style:{backgroundColor:"transparent"}},null==(t=e.tabs)?void 0:t.map((t=>(e.usesRouter||g)&&t.usesRouter?(0,h.tZ)(b.v.Item,{key:t.label},(0,h.tZ)("li",{role:"tab",className:t.name===e.activeChild?"active":""},(0,h.tZ)("div",null,(0,h.tZ)(o.rU,{to:t.url||""},t.label)))):(0,h.tZ)(b.v.Item,{key:t.label},(0,h.tZ)("li",{className:c()("no-router",{active:t.name===e.activeChild}),role:"tab"},(0,h.tZ)("a",{href:t.url,onClick:t.onClick},t.label)))))),(0,h.tZ)("div",{className:s},null==(a=e.buttons)?void 0:a.map(((e,t)=>(0,h.tZ)(f.Z,{key:t,buttonStyle:e.buttonStyle,onClick:e.onClick},e.name))))),e.children)}},40164:(e,t,a)=>{"use strict";var i,n=a(67294),r=a(90731),d=a(5872),o=a.n(d),l=a(73727),s=a(5977),c=a(91877),u=a(57902),b=a(38703),f=a(56052),h=a(85156),m=a(5951),p=a(65286),g=a(93185),v=a(43063),Z=a.n(v),y=a(51995),_=a(61988),w=a(43700),x=a(61337),C=a(55467),S=a(14114),E=a(40768),k=a(4715),T=a(30381),I=a.n(T),$=a(20755),N=a(70163),D=a(35932);!function(e){e.Charts="CHARTS",e.Dashboards="DASHBOARDS",e.Recents="RECENTS",e.SavedQueries="SAVED_QUERIES"}(i||(i={}));var F=a(11965);const R={[i.Charts]:(0,_.t)("charts"),[i.Dashboards]:(0,_.t)("dashboards"),[i.Recents]:(0,_.t)("recents"),[i.SavedQueries]:(0,_.t)("saved queries")},L=y.iK.div`
  min-height: 200px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
`,U=y.iK.div`
  Button {
    svg {
      color: ${({theme:e})=>e.colors.grayscale.light5};
    }
  }
`;function z({tableName:e,tab:t}){const a={[i.Charts]:"/chart/add",[i.Dashboards]:"/dashboard/new",[i.SavedQueries]:"/superset/sqllab?new=true"},n={[i.Charts]:"/chart/list",[i.Dashboards]:"/dashboard/list/",[i.SavedQueries]:"/savedqueryview/list/"},r={[i.Charts]:"empty-charts.svg",[i.Dashboards]:"empty-dashboard.svg",[i.Recents]:"union.svg",[i.SavedQueries]:"empty-queries.svg"},d=(0,F.tZ)("span",null,(0,_.t)("No %(tableName)s yet",{tableName:R[e]})),o=(0,F.tZ)("span",{className:"no-recents"},"Viewed"===t?(0,_.t)("Recently viewed charts, dashboards, and saved queries will appear here"):"Created"===t?(0,_.t)("Recently created charts, dashboards, and saved queries will appear here"):"Examples"===t?(0,_.t)("Example %(tableName)s will appear here",{tableName:e.toLowerCase()}):"Edited"===t?(0,_.t)("Recently edited charts, dashboards, and saved queries will appear here"):null);return"Mine"===t||"RECENTS"===e||"Examples"===t?(0,F.tZ)(L,null,(0,F.tZ)(k.HY,{image:`/static/assets/images/${r[e]}`,description:"RECENTS"===e||"Examples"===t?o:d},"RECENTS"!==e&&(0,F.tZ)(U,null,(0,F.tZ)(D.Z,{buttonStyle:"primary",onClick:()=>{window.location.href=a[e]}},(0,F.tZ)("i",{className:"fa fa-plus"}),"SAVED_QUERIES"===e?(0,_.t)("SQL query"):(0,_.t)(`${e.split("").slice(0,e.length-1).join("")}\n                    `))))):(0,F.tZ)(L,null,(0,F.tZ)(k.HY,{image:"/static/assets/images/star-circle.svg",description:(0,F.tZ)("span",{className:"no-favorites"},(0,_.t)("You don't have any favorites yet!"))},(0,F.tZ)(D.Z,{buttonStyle:"primary",onClick:()=>{window.location.href=n[e]}},(0,_.t)("See all %(tableName)s",{tableName:"SAVED_QUERIES"===e?(0,_.t)("SQL Lab queries"):R[e]}))))}var A;!function(e){e.EDITED="Edited",e.CREATED="Created",e.VIEWED="Viewed",e.EXAMPLE="Examples"}(A||(A={}));const P=y.iK.div`
  .recentCards {
    max-height: none;
    grid-gap: ${({theme:e})=>4*e.gridUnit+"px"};
  }
`,M=(0,_.t)("[Untitled]"),q=(0,_.t)("Unknown"),O=e=>"dashboard_title"in e?e.dashboard_title||M:"slice_name"in e?e.slice_name||M:"label"in e?e.label||M:e.item_title||M,j=e=>{if("sql"in e)return(0,F.tZ)(N.Z.Sql,null);const t="item_url"in e?e.item_url:e.url;return null!=t&&t.includes("dashboard")?(0,F.tZ)(N.Z.NavDashboard,null):null!=t&&t.includes("explore")?(0,F.tZ)(N.Z.NavCharts,null):null};function V({activeChild:e,setActiveChild:t,activityData:a,user:r,loadedCount:d}){var o;const[l,s]=(0,n.useState)(),[c,u]=(0,n.useState)(!1);(0,n.useEffect)((()=>{"Edited"===e&&(u(!0),u(!0),(0,E.Ld)(r.userId).then((e=>{s([...e.editedChart,...e.editedDash]),u(!1)})))}),[e]);const b=[{name:"Edited",label:(0,_.t)("Edited"),onClick:()=>{t("Edited"),(0,x.LS)(x.dR.homepage_activity_filter,A.EDITED)}},{name:"Created",label:(0,_.t)("Created"),onClick:()=>{t("Created"),(0,x.LS)(x.dR.homepage_activity_filter,A.CREATED)}}];return null!=a&&a.Viewed&&b.unshift({name:"Viewed",label:(0,_.t)("Viewed"),onClick:()=>{t("Viewed"),(0,x.LS)(x.dR.homepage_activity_filter,A.VIEWED)}}),c&&!l||d<3?(0,F.tZ)(me,null):(0,F.tZ)(P,null,(0,F.tZ)($.Z,{activeChild:e,tabs:b}),(null==(o=a[e])?void 0:o.length)>0||"Edited"===e&&l&&l.length>0?(0,F.tZ)(E._L,{className:"recentCards"},("Edited"!==e?a[e]:l).map((e=>{const t=(e=>"sql"in e?`/superset/sqllab?savedQueryId=${e.id}`:"url"in e?e.url:e.item_url)(e),a=(e=>{if("time"in e)return(0,_.t)("Viewed %s",I()(e.time).fromNow());let t;return"changed_on"in e&&(t=e.changed_on),"changed_on_utc"in e&&(t=e.changed_on_utc),(0,_.t)("Modified %s",null==t?q:I()(t).fromNow())})(e);return(0,F.tZ)(E.ZB,{onClick:()=>{window.location.href=t},key:t},(0,F.tZ)(C.Z,{cover:(0,F.tZ)(n.Fragment,null),url:t,title:O(e),description:a,avatar:j(e),actions:null}))}))):(0,F.tZ)(z,{tableName:i.Recents,tab:e}))}var B=a(63105),K=a.n(B),H=a(34858),Q=a(12),X=a(83673),Y=a(34024),W=a(32228);const J=(0,S.Z)((function({user:e,addDangerToast:t,addSuccessToast:a,mine:r,showThumbnails:d,examples:o}){const l=(0,s.k6)(),c=(0,x.rV)(x.dR.homepage_chart_filter,Q.s.EXAMPLES),f=K()(o,(e=>"viz_type"in e)),{state:{loading:h,resourceCollection:m,bulkSelectEnabled:p},setResourceCollection:g,hasPerm:v,refreshData:Z,fetchData:y}=(0,H.Yi)("chart",(0,_.t)("chart"),t,!0,"Mine"===c?r:f,[],!1),w=(0,n.useMemo)((()=>m.map((e=>e.id))),[m]),[C,S]=(0,H.NE)("chart",w,t),{sliceCurrentlyEditing:k,openChartEditModal:T,handleChartUpdated:I,closeChartEditModal:N}=(0,H.fF)(g,m),[D,R]=(0,n.useState)(c),[L,U]=(0,n.useState)(!1),[A,P]=(0,n.useState)(!1);(0,n.useEffect)((()=>{(A||"Favorite"===D)&&O(D),P(!0)}),[D]);const M=e=>{const t=e.map((({id:e})=>e));(0,W.Z)("chart",t,(()=>{U(!1)})),U(!0)},q=t=>{const a=[];return"Mine"===t?a.push({id:"created_by",operator:"rel_o_m",value:`${null==e?void 0:e.userId}`}):"Favorite"===t?a.push({id:"id",operator:"chart_is_favorite",value:!0}):"Examples"===t&&a.push({id:"created_by",operator:"rel_o_m",value:0}),a},O=e=>y({pageIndex:0,pageSize:E.IV,sortBy:[{id:"changed_on_delta_humanized",desc:!0}],filters:q(e)}),j=[{name:"Favorite",label:(0,_.t)("Favorite"),onClick:()=>{R(Q.s.FAVORITE),(0,x.LS)(x.dR.homepage_chart_filter,Q.s.FAVORITE)}},{name:"Mine",label:(0,_.t)("Mine"),onClick:()=>{R(Q.s.MINE),(0,x.LS)(x.dR.homepage_chart_filter,Q.s.MINE)}}];return o&&j.push({name:"Examples",label:(0,_.t)("Examples"),onClick:()=>{R(Q.s.EXAMPLES),(0,x.LS)(x.dR.homepage_chart_filter,Q.s.EXAMPLES)}}),h?(0,F.tZ)(me,{cover:d}):(0,F.tZ)(u.Z,null,k&&(0,F.tZ)(X.Z,{onHide:N,onSave:I,show:!0,slice:k}),(0,F.tZ)($.Z,{activeChild:D,tabs:j,buttons:[{name:(0,F.tZ)(n.Fragment,null,(0,F.tZ)("i",{className:"fa fa-plus"}),(0,_.t)("Chart")),buttonStyle:"tertiary",onClick:()=>{window.location.assign("/chart/add")}},{name:(0,_.t)("View All »"),buttonStyle:"link",onClick:()=>{const e="Favorite"===D?`/chart/list/?filters=(favorite:(label:${(0,_.t)("Yes")},value:!t))`:"/chart/list/";l.push(e)}}]}),null!=m&&m.length?(0,F.tZ)(E._L,{showThumbnails:d},m.map((i=>(0,F.tZ)(Y.Z,{key:`${i.id}`,openChartEditModal:T,chartFilter:D,chart:i,userId:null==e?void 0:e.userId,hasPerm:v,showThumbnails:d,bulkSelectEnabled:p,refreshData:Z,addDangerToast:t,addSuccessToast:a,favoriteStatus:S[i.id],saveFavoriteStatus:C,handleBulkChartExport:M})))):(0,F.tZ)(z,{tableName:i.Charts,tab:D}),L&&(0,F.tZ)(b.Z,null))}));var G=a(31069),ee=a(42110),te=a(33743),ae=a(120),ie=a(83862),ne=a(17198);ee.Z.registerLanguage("sql",te.Z);const re=y.iK.div`
  cursor: pointer;
  a {
    text-decoration: none;
  }
  .ant-card-cover {
    border-bottom: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
    & > div {
      height: 171px;
    }
  }
  .gradient-container > div {
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    background-color: ${({theme:e})=>e.colors.secondary.light3};
    display: inline-block;
    width: 100%;
    height: 179px;
    background-repeat: no-repeat;
    vertical-align: middle;
  }
`,de=y.iK.div`
  svg {
    margin-left: ${({theme:e})=>10*e.gridUnit}px;
  }
  .query-title {
    padding: ${({theme:e})=>2*e.gridUnit+2}px;
    font-size: ${({theme:e})=>e.typography.sizes.l}px;
  }
`,oe=y.iK.div`
  pre {
    height: ${({theme:e})=>40*e.gridUnit}px;
    border: none !important;
    background-color: ${({theme:e})=>e.colors.grayscale.light5} !important;
    overflow: hidden;
    padding: ${({theme:e})=>4*e.gridUnit}px !important;
  }
`,le=(0,S.Z)((({user:e,addDangerToast:t,addSuccessToast:a,mine:r,showThumbnails:d,featureFlag:o})=>{const{state:{loading:l,resourceCollection:s},hasPerm:c,fetchData:u,refreshData:b}=(0,H.Yi)("saved_query",(0,_.t)("query"),t,!0,r,[],!1),[f,h]=(0,n.useState)("Mine"),[m,p]=(0,n.useState)(!1),[g,v]=(0,n.useState)({}),[Z,w]=(0,n.useState)(!0),x=c("can_edit"),S=c("can_delete"),T=(0,y.Fg)(),I=t=>{const a=[];return"Mine"===t?a.push({id:"created_by",operator:"rel_o_m",value:`${null==e?void 0:e.userId}`}):a.push({id:"id",operator:"saved_query_is_fav",value:!0}),a};return l?(0,F.tZ)(me,{cover:d}):(0,F.tZ)(n.Fragment,null,m&&(0,F.tZ)(ne.Z,{description:(0,_.t)("This action will permanently delete the saved query."),onConfirm:()=>{m&&(({id:i,label:n})=>{G.Z.delete({endpoint:`/api/v1/saved_query/${i}`}).then((()=>{const t={filters:[{id:"created_by",operator:"rel_o_m",value:`${null==e?void 0:e.userId}`}],pageSize:E.IV,sortBy:[{id:"changed_on_delta_humanized",desc:!0}],pageIndex:0};b(Z?t:void 0),w(!1),p(!1),a((0,_.t)("Deleted: %s",n))}),(0,E.v$)((e=>t((0,_.t)("There was an issue deleting %s: %s",n,e)))))})(g)},onHide:()=>{p(!1)},open:!0,title:(0,_.t)("Delete Query?")}),(0,F.tZ)($.Z,{activeChild:f,tabs:[{name:"Mine",label:(0,_.t)("Mine"),onClick:()=>u({pageIndex:0,pageSize:E.IV,sortBy:[{id:"changed_on_delta_humanized",desc:!0}],filters:I("Mine")}).then((()=>h("Mine")))}],buttons:[{name:(0,F.tZ)(n.Fragment,null,(0,F.tZ)("i",{className:"fa fa-plus"}),(0,_.t)("SQL Query")),buttonStyle:"tertiary",onClick:()=>{window.location.href="/superset/sqllab?new=true"}},{name:(0,_.t)("View All »"),buttonStyle:"link",onClick:()=>{window.location.href="/savedqueryview/list"}}]}),s.length>0?(0,F.tZ)(E._L,{showThumbnails:d},s.map((e=>{var i,r,l;return(0,F.tZ)(re,{onClick:()=>{window.location.href=`/superset/sqllab?savedQueryId=${e.id}`},key:e.id},(0,F.tZ)(C.Z,{imgURL:"",url:`/superset/sqllab?savedQueryId=${e.id}`,title:e.label,imgFallbackURL:"/static/assets/images/empty-query.svg",description:(0,_.t)("Ran %s",e.changed_on_delta_humanized),cover:null!=e&&null!=(i=e.sql)&&i.length&&d&&o?(0,F.tZ)(oe,null,(0,F.tZ)(ee.Z,{language:"sql",lineProps:{style:{color:"black",wordBreak:"break-all",whiteSpace:"pre-wrap"}},style:ae.Z,wrapLines:!0,lineNumberStyle:{display:"none"},showLineNumbers:!1},(0,E.IB)(e.sql,25))):!(d&&(null==e||null==(r=e.sql)||!r.length))&&(0,F.tZ)(n.Fragment,null),actions:(0,F.tZ)(de,null,(0,F.tZ)(C.Z.Actions,{onClick:e=>{e.stopPropagation(),e.preventDefault()}},(0,F.tZ)(k.Gj,{overlay:(l=e,(0,F.tZ)(ie.v,null,x&&(0,F.tZ)(ie.v.Item,{onClick:()=>{window.location.href=`/superset/sqllab?savedQueryId=${l.id}`}},(0,_.t)("Edit")),(0,F.tZ)(ie.v.Item,{onClick:()=>{l.id&&(0,H.bR)(l.id,t,a)}},(0,_.t)("Share")),S&&(0,F.tZ)(ie.v.Item,{onClick:()=>{p(!0),v(l)}},(0,_.t)("Delete"))))},(0,F.tZ)(N.Z.MoreVert,{iconColor:T.colors.grayscale.base}))))}))}))):(0,F.tZ)(z,{tableName:i.SavedQueries,tab:f}))}));var se=a(20818),ce=a(99415);const ue=(0,S.Z)((function({user:e,addDangerToast:t,addSuccessToast:a,mine:r,showThumbnails:d,examples:o}){const l=(0,s.k6)(),c=(0,x.rV)(x.dR.homepage_dashboard_filter,Q.s.EXAMPLES),u=K()(o,(e=>!("viz_type"in e))),{state:{loading:f,resourceCollection:h},setResourceCollection:m,hasPerm:p,refreshData:g,fetchData:v}=(0,H.Yi)("dashboard",(0,_.t)("dashboard"),t,!0,"Mine"===c?r:u,[],!1),Z=(0,n.useMemo)((()=>h.map((e=>e.id))),[h]),[y,w]=(0,H.NE)("dashboard",Z,t),[C,S]=(0,n.useState)(),[k,T]=(0,n.useState)(c),[I,N]=(0,n.useState)(!1),[D,R]=(0,n.useState)(!1);(0,n.useEffect)((()=>{(D||"Favorite"===k)&&P(k),R(!0)}),[k]);const L=e=>{const t=e.map((({id:e})=>e));(0,W.Z)("dashboard",t,(()=>{N(!1)})),N(!0)},U=t=>{const a=[];return"Mine"===t?a.push({id:"created_by",operator:"rel_o_m",value:`${null==e?void 0:e.userId}`}):"Favorite"===t?a.push({id:"id",operator:"dashboard_is_favorite",value:!0}):"Examples"===t&&a.push({id:"created_by",operator:"rel_o_m",value:0}),a},A=[{name:"Favorite",label:(0,_.t)("Favorite"),onClick:()=>{T(Q.s.FAVORITE),(0,x.LS)(x.dR.homepage_dashboard_filter,Q.s.FAVORITE)}},{name:"Mine",label:(0,_.t)("Mine"),onClick:()=>{T(Q.s.MINE),(0,x.LS)(x.dR.homepage_dashboard_filter,Q.s.MINE)}}];o&&A.push({name:"Examples",label:(0,_.t)("Examples"),onClick:()=>{T(Q.s.EXAMPLES),(0,x.LS)(x.dR.homepage_dashboard_filter,Q.s.EXAMPLES)}});const P=e=>v({pageIndex:0,pageSize:E.IV,sortBy:[{id:"changed_on_delta_humanized",desc:!0}],filters:U(e)});return f?(0,F.tZ)(me,{cover:d}):(0,F.tZ)(n.Fragment,null,(0,F.tZ)($.Z,{activeChild:k,tabs:A,buttons:[{name:(0,F.tZ)(n.Fragment,null,(0,F.tZ)("i",{className:"fa fa-plus"}),(0,_.t)("Dashboard")),buttonStyle:"tertiary",onClick:()=>{window.location.assign("/dashboard/new")}},{name:(0,_.t)("View All »"),buttonStyle:"link",onClick:()=>{const e="Favorite"===k?`/dashboard/list/?filters=(favorite:(label:${(0,_.t)("Yes")},value:!t))`:"/dashboard/list/";l.push(e)}}]}),C&&(0,F.tZ)(se.Z,{dashboardId:null==C?void 0:C.id,show:!0,onHide:()=>S(void 0),onSubmit:e=>G.Z.get({endpoint:`/api/v1/dashboard/${e.id}`}).then((({json:e={}})=>{m(h.map((t=>t.id===e.id?e.result:t)))}),(0,E.v$)((e=>t((0,_.t)("An error occurred while fetching dashboards: %s",e)))))}),h.length>0&&(0,F.tZ)(E._L,{showThumbnails:d},h.map((i=>(0,F.tZ)(ce.Z,{key:i.id,dashboard:i,hasPerm:p,bulkSelectEnabled:!1,showThumbnails:d,dashboardFilter:k,refreshData:g,addDangerToast:t,addSuccessToast:a,userId:null==e?void 0:e.userId,loading:f,openDashboardEditModal:e=>S(e),saveFavoriteStatus:y,favoriteStatus:w[i.id],handleBulkDashboardExport:L})))),0===h.length&&(0,F.tZ)(z,{tableName:i.Dashboards,tab:k}),I&&(0,F.tZ)(b.Z,null))})),be=["2","3"],fe=y.iK.div`
  background-color: ${({theme:e})=>e.colors.grayscale.light4};
  .ant-row.menu {
    margin-top: -15px;
    background-color: ${({theme:e})=>e.colors.grayscale.light4};
    &:after {
      content: '';
      display: block;
      border: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
      margin: 0px ${({theme:e})=>6*e.gridUnit}px;
      position: relative;
      width: 100%;
      ${E.mq[1]} {
        margin-top: 5px;
        margin: 0px 2px;
      }
    }
    .ant-menu.ant-menu-light.ant-menu-root.ant-menu-horizontal {
      padding-left: ${({theme:e})=>8*e.gridUnit}px;
    }
    button {
      padding: 3px 21px;
    }
  }
  .ant-card-meta-description {
    margin-top: ${({theme:e})=>e.gridUnit}px;
  }
  .ant-card.ant-card-bordered {
    border: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
  }
  .ant-collapse-item .ant-collapse-content {
    margin-bottom: ${({theme:e})=>-6*e.gridUnit}px;
  }
  div.ant-collapse-item:last-child.ant-collapse-item-active
    .ant-collapse-header {
    padding-bottom: ${({theme:e})=>3*e.gridUnit}px;
  }
  div.ant-collapse-item:last-child .ant-collapse-header {
    padding-bottom: ${({theme:e})=>9*e.gridUnit}px;
  }
  .loading-cards {
    margin-top: ${({theme:e})=>8*e.gridUnit}px;
    .ant-card-cover > div {
      height: 168px;
    }
  }
`,he=y.iK.div`
  height: 50px;
  background-color: white;
  .navbar-brand {
    margin-left: ${({theme:e})=>2*e.gridUnit}px;
    font-weight: ${({theme:e})=>e.typography.weights.bold};
  }
  .switch {
    float: right;
    margin: ${({theme:e})=>5*e.gridUnit}px;
    display: flex;
    flex-direction: row;
    span {
      display: block;
      margin: ${({theme:e})=>1*e.gridUnit}px;
      line-height: 1;
    }
  }
`,me=({cover:e})=>(0,F.tZ)(E._L,{showThumbnails:e,className:"loading-cards"},[...new Array(E.iv)].map((()=>(0,F.tZ)(C.Z,{cover:!e&&(0,F.tZ)(n.Fragment,null),description:"",loading:!0})))),pe=(0,S.Z)((function({user:e,addDangerToast:t}){const a=e.userId.toString(),i=`/superset/recent_activity/${e.userId}/?limit=6`,[r,d]=(0,n.useState)("Loading"),o=(0,x.OH)(a,null);let l=!1;(0,c.cr)(g.T.THUMBNAILS)&&(l=void 0===(null==o?void 0:o.thumbnails)||(null==o?void 0:o.thumbnails));const[s,u]=(0,n.useState)(l),[b,f]=(0,n.useState)(null),[h,m]=(0,n.useState)(null),[p,v]=(0,n.useState)(null),[y,C]=(0,n.useState)(null),[S,T]=(0,n.useState)(0),I=(0,x.rV)(x.dR.homepage_collapse_state,[]),[$,N]=(0,n.useState)(I);(0,n.useEffect)((()=>{const n=(0,x.rV)(x.dR.homepage_activity_filter,null);N(I.length>0?I:be),(0,E.Hn)(e.userId,i,t).then((e=>{const t={};if(t.Examples=e.examples,e.viewed){const a=Z()(e.viewed,["item_url",null]).map((e=>e));t.Viewed=a,!n&&t.Viewed?d("Viewed"):n||t.Viewed?d(n||"Created"):d("Created")}else d(n||"Created");f((e=>({...e,...t})))})).catch((0,E.v$)((e=>{f((e=>({...e,Viewed:[]}))),t((0,_.t)("There was an issue fetching your recent activity: %s",e))}))),(0,E.B1)(a,"dashboard").then((e=>{C(e),T((e=>e+1))})).catch((e=>{C([]),T((e=>e+1)),t((0,_.t)("There was an issues fetching your dashboards: %s",e))})),(0,E.B1)(a,"chart").then((e=>{m(e),T((e=>e+1))})).catch((e=>{m([]),T((e=>e+1)),t((0,_.t)("There was an issues fetching your chart: %s",e))})),(0,E.B1)(a,"saved_query").then((e=>{v(e),T((e=>e+1))})).catch((e=>{v([]),T((e=>e+1)),t((0,_.t)("There was an issues fetching your saved queries: %s",e))}))}),[]),(0,n.useEffect)((()=>{!I&&null!=p&&p.length&&N((e=>[...e,"4"])),f((e=>({...e,Created:[...(null==h?void 0:h.slice(0,3))||[],...(null==y?void 0:y.slice(0,3))||[],...(null==p?void 0:p.slice(0,3))||[]]})))}),[h,p,y]),(0,n.useEffect)((()=>{var e;!I&&null!=b&&null!=(e=b.Viewed)&&e.length&&N((e=>["1",...e]))}),[b]);const D=!(null!=b&&b.Examples||null!=b&&b.Viewed);return(0,F.tZ)(fe,null,(0,F.tZ)(he,null,(0,F.tZ)("span",{className:"navbar-brand"},"Home"),(0,c.cr)(g.T.THUMBNAILS)?(0,F.tZ)("div",{className:"switch"},(0,F.tZ)(k.KU,{checked:s,onChange:()=>{u(!s),(0,x.I_)(a,{thumbnails:!s})}}),(0,F.tZ)("span",null,"Thumbnails")):null),(0,F.tZ)(w.Z,{activeKey:$,onChange:e=>{N(e),(0,x.LS)(x.dR.homepage_collapse_state,e)},ghost:!0,bigger:!0},(0,F.tZ)(w.Z.Panel,{header:(0,_.t)("Recents"),key:"1"},b&&(b.Viewed||b.Examples||b.Created)&&"Loading"!==r?(0,F.tZ)(V,{user:e,activeChild:r,setActiveChild:d,activityData:b,loadedCount:S}):(0,F.tZ)(me,null)),(0,F.tZ)(w.Z.Panel,{header:(0,_.t)("Dashboards"),key:"2"},!y||D?(0,F.tZ)(me,{cover:s}):(0,F.tZ)(ue,{user:e,mine:y,showThumbnails:s,examples:null==b?void 0:b.Examples})),(0,F.tZ)(w.Z.Panel,{header:(0,_.t)("Charts"),key:"3"},!h||D?(0,F.tZ)(me,{cover:s}):(0,F.tZ)(J,{showThumbnails:s,user:e,mine:h,examples:null==b?void 0:b.Examples})),(0,F.tZ)(w.Z.Panel,{header:(0,_.t)("Saved queries"),key:"4"},p?(0,F.tZ)(le,{showThumbnails:s,user:e,mine:p,featureFlag:(0,c.cr)(g.T.THUMBNAILS)}):(0,F.tZ)(me,{cover:s}))))})),ge=(0,n.lazy)((()=>Promise.all([a.e(8289),a.e(4787)]).then(a.bind(a,28999)))),ve=(0,n.lazy)((()=>Promise.all([a.e(1216),a.e(876),a.e(8289),a.e(9502)]).then(a.bind(a,63082)))),Ze=(0,n.lazy)((()=>Promise.all([a.e(8289),a.e(1611)]).then(a.bind(a,35276)))),ye=(0,n.lazy)((()=>Promise.all([a.e(1216),a.e(504),a.e(2087),a.e(3212),a.e(8289),a.e(674),a.e(1629),a.e(665)]).then(a.bind(a,13434)))),_e=(0,n.lazy)((()=>Promise.all([a.e(8289),a.e(9452)]).then(a.bind(a,69053)))),we=(0,n.lazy)((()=>Promise.all([a.e(193),a.e(8289),a.e(8774)]).then(a.bind(a,23767)))),xe=(0,n.lazy)((()=>Promise.all([a.e(1216),a.e(504),a.e(2087),a.e(3212),a.e(674),a.e(1629),a.e(5296)]).then(a.bind(a,37936)))),Ce=(0,n.lazy)((()=>Promise.all([a.e(8289),a.e(4502)]).then(a.bind(a,30075)))),Se=(0,n.lazy)((()=>Promise.all([a.e(8289),a.e(5656)]).then(a.bind(a,97894)))),Ee=(0,n.lazy)((()=>Promise.all([a.e(8289),a.e(9137)]).then(a.bind(a,25163)))),ke=(0,n.lazy)((()=>Promise.all([a.e(8289),a.e(4173),a.e(7633)]).then(a.bind(a,82842)))),Te=[{path:"/superset/welcome/",Component:pe},{path:"/dashboard/list/",Component:we},{path:"/superset/dashboard/:idOrSlug/",Component:xe},{path:"/chart/list/",Component:ye},{path:"/tablemodelview/list/",Component:Se},{path:"/databaseview/list/",Component:Ce},{path:"/savedqueryview/list/",Component:(0,n.lazy)((()=>Promise.all([a.e(8289),a.e(4173),a.e(9173)]).then(a.bind(a,49588))))},{path:"/csstemplatemodelview/list/",Component:_e},{path:"/annotationlayermodelview/list/",Component:ge},{path:"/annotationmodelview/:annotationLayerId/annotation/",Component:Ze},{path:"/superset/sqllab/history/",Component:ke},{path:"/alert/list/",Component:ve},{path:"/report/list/",Component:ve,props:{isReportEnabled:!0}},{path:"/alert/:alertId/log/",Component:Ee},{path:"/report/:alertId/log/",Component:Ee,props:{isReportEnabled:!0}}],Ie=Te.map((e=>e.path)).reduce(((e,t)=>({...e,[t]:!0})),{});function $e(e){if(!(0,c.cr)(g.T.ENABLE_REACT_CRUD_VIEWS))return!1;if(e){const t=e.split(/[?#]/)[0];return!!Ie[t]}return!1}var Ne=a(3741),De=a(68135),Fe=a(37703),Re=a(35755),Le=a(38626),Ue=a(57865),ze=a(89474),Ae=a(33626);const Pe={info:"addInfoToast",alert:"addDangerToast",danger:"addDangerToast",warning:"addWarningToast",success:"addSuccessToast"};function Me({children:e,messages:t}){const a=(0,S.e)();return(0,Ae.J)((()=>{t.forEach((e=>{const[t,i]=e,n=a[Pe[t]];n&&n(i)}))})),e}var qe=a(29147),Oe=a(14278);const je={...h.b.common},Ve=({children:e})=>(0,F.tZ)(De.a,{theme:h.r},(0,F.tZ)(Fe.zt,{store:ze.h},(0,F.tZ)(Le.W,{backend:Ue.PD},(0,F.tZ)(Me,{messages:je.flash_messages},(0,F.tZ)(qe.DG,null,(0,F.tZ)(Oe.EM,null,(0,F.tZ)(Re.Fz,{ReactRouterRoute:s.AW,stringifyOptions:{encode:!1}},e)))))));(0,p.Z)();const Be={...h.b.user},Ke={...h.b.common.menu_data};let He;(0,c.fG)(h.b.common.feature_flags);const Qe=()=>{const e=(0,s.TH)();return(0,n.useEffect)((()=>{He&&He!==e.pathname&&Ne.Yd.markTimeOrigin(),He=e.pathname}),[e.pathname]),(0,F.tZ)(n.Fragment,null)};r.render((0,F.tZ)((()=>(0,F.tZ)(l.VK,null,(0,F.tZ)(Qe,null),(0,F.tZ)(Ve,null,(0,F.tZ)(f.Z,{data:Ke,isFrontendRoute:$e}),(0,F.tZ)(s.rs,null,Te.map((({path:e,Component:t,props:a={},Fallback:i=b.Z})=>(0,F.tZ)(s.AW,{path:e,key:e},(0,F.tZ)(n.Suspense,{fallback:(0,F.tZ)(i,null)},(0,F.tZ)(u.Z,null,(0,F.tZ)(t,o()({user:Be},a)))))))),(0,F.tZ)(m.Z,null)))),null),document.getElementById("app"))}},s={};function c(e){var t=s[e];if(void 0!==t)return t.exports;var a=s[e]={id:e,loaded:!1,exports:{}};return l[e].call(a.exports,a,a.exports,c),a.loaded=!0,a.exports}c.m=l,c.amdD=function(){throw new Error("define cannot be used indirect")},c.amdO={},e=[],c.O=(t,a,i,n)=>{if(!a){var r=1/0;for(s=0;s<e.length;s++){for(var[a,i,n]=e[s],d=!0,o=0;o<a.length;o++)(!1&n||r>=n)&&Object.keys(c.O).every((e=>c.O[e](a[o])))?a.splice(o--,1):(d=!1,n<r&&(r=n));if(d){e.splice(s--,1);var l=i();void 0!==l&&(t=l)}}return t}n=n||0;for(var s=e.length;s>0&&e[s-1][2]>n;s--)e[s]=e[s-1];e[s]=[a,i,n]},c.H={},c.G=e=>{Object.keys(c.H).map((t=>{c.H[t](e)}))},c.n=e=>{var t=e&&e.__esModule?()=>e.default:()=>e;return c.d(t,{a:t}),t},a=Object.getPrototypeOf?e=>Object.getPrototypeOf(e):e=>e.__proto__,c.t=function(e,i){if(1&i&&(e=this(e)),8&i)return e;if("object"==typeof e&&e){if(4&i&&e.__esModule)return e;if(16&i&&"function"==typeof e.then)return e}var n=Object.create(null);c.r(n);var r={};t=t||[null,a({}),a([]),a(a)];for(var d=2&i&&e;"object"==typeof d&&!~t.indexOf(d);d=a(d))Object.getOwnPropertyNames(d).forEach((t=>r[t]=()=>e[t]));return r.default=()=>e,c.d(n,r),n},c.d=(e,t)=>{for(var a in t)c.o(t,a)&&!c.o(e,a)&&Object.defineProperty(e,a,{enumerable:!0,get:t[a]})},c.f={},c.e=e=>Promise.all(Object.keys(c.f).reduce(((t,a)=>(c.f[a](e,t),t)),[])),c.u=e=>2087===e?"2087.c57929e84c0056c13f96.entry.js":4593===e?"4593.2781346fcc306d505925.entry.js":674===e?"674.04d8a5772e8d0491d27c.entry.js":2671===e?"2671.1b219d63906984859ee6.entry.js":876===e?"876.7e7648363c67248b070b.entry.js":504===e?"thumbnail.d421499737462f4dd598.entry.js":3212===e?"3212.eccc3fc35efc78cfe8ed.entry.js":1629===e?"1629.4dfa4d7d027ae468c3bc.entry.js":2441===e?"2441.cf2d2dd99eca21c7005d.entry.js":1163===e?"1163.bb2e8b62ec4fe3b9f038.entry.js":4443===e?"4443.3a81f9e6c843b22c7a0e.entry.js":{57:"3eef258f00447ab2ba56",112:"881dd2510f19ed31e172",158:"488593bc94ab7caa58e0",177:"4b03c272091be7836683",183:"3f0101a74920ebdf5721",193:"71f8844c3013f9106381",215:"abe0f2a4a3f69594f00c",310:"77d6d4c65a4250a67f54",312:"ba5d653bdbc1bcc11798",326:"7f70cded66eafbdda58b",336:"f4bdd4f606d6d7592f7e",347:"5c3072822b5d502ad29e",349:"31b11e55a94ab02f4dfe",363:"210381fc4c2bbae6d099",380:"78b7b6dc715440560460",435:"d80842b3792be4e68b96",440:"515662946aea2cdc4413",444:"fa4262dbba7f89704a67",452:"258cd8cc24edac1875e0",597:"20b87c137727ff9aaf87",600:"044558ce92babe1fa2db",616:"1dd1ec932ddf52008657",665:"0d95e487a612770c8bdd",704:"ea4830f53c7e29617097",775:"8b50482b2ca8f4987b2a",826:"0e2f19bbb57b5a8aff83",895:"1f77c3c8dcb2024e6e96",954:"60c8e389f3d779b44283",992:"d71578d87db841083c93",999:"ce189cf323818358d600",1020:"72ffbeec3df47e34e0e0",1075:"2572ea51a4adfc4ff9a4",1095:"b533f258ca6b1a324379",1130:"fa987d26b147137ea4a2",1174:"1033573182d374214540",1185:"63e33afadbeb6e51d8dd",1221:"b9936995d898af34e03c",1256:"035f322d4ce964f73de1",1258:"6381160c0229525565fd",1263:"cfe95e8e20298feb874e",1293:"14b3a7ee4cc17de5c441",1351:"2eb1a9ba1648eb7a8193",1382:"dff5a1149875c367ecda",1398:"0c371615e0996614785c",1493:"0c0664678b66d74ba38f",1497:"f64aaa6444c4f5d90950",1568:"b2bb81324e29ed5bce61",1573:"c893b7f636a2ab701c65",1605:"d6a140bf5e3bef201212",1611:"a802107d23eb93db8386",1862:"8b03e8bb1c84992cbf32",1877:"e33515e5bd6542b94f77",1899:"e1eb313fc03e90fa0d70",1948:"e8e04804b69cd452fcc9",2045:"2e374ea725d1d98f2dc1",2079:"579cd7268aa39862c290",2089:"13db7039a066b543f45a",2105:"02df5ff9f97c181f9de4",2112:"1d1b4aaac5752d48445e",2229:"edca9d5a70fe57e9deb1",2264:"5a90b87bf6c82cddd60f",2267:"58a5465f711b4c6b0f0c",2403:"ff967bce10197be4d6e0",2439:"92ff10820007284a3594",2646:"3dcaf7b2edc6b26550ba",2698:"e7b7a6eeb3966de7d0c1",2713:"a68c27cd1e12e64ffed4",2797:"5db241c8af5a71f0f30d",2983:"8afbd45ac5fc6d8b4b6d",3126:"db7e749de1e103f1aff8",3141:"494a0ca0a1bb39f625bd",3208:"2afd52e561441bd5beb3",3232:"da20088427ef3c3faab7",3240:"e7218edd46dedf7e1dda",3265:"1671e36958a7bf6f4cfc",3325:"9295baeedc623870f610",3496:"31f39cd73e24732b2940",3501:"b1f59c8250c7436d58a1",3544:"0fb4e4d961165cd76e18",3558:"e2f6e711a397fa768c21",3567:"d77d0432d12254aeeded",3606:"0b65905a659b39cd6909",3711:"0f0dbeed171be7ec0dee",3745:"03ab023678c0223d3569",3749:"9d45482bb7e08b4be181",3811:"dd0d3e1829322848d982",3871:"b94982d813b3a1874fe0",3955:"afc2c2846692569a5718",3985:"f293395f2172b1317b51",3986:"b65058c809eb4184aab8",4139:"285945130a72bfc46e1d",4173:"a9c03588da6793bd9e1b",4194:"0e16885080d878e0abd0",4266:"5b30930400b0988390e0",4273:"7ddbd55189a7899df93c",4458:"4309988c3c4fa37de107",4474:"b598fc6c061ecd9e6b0d",4502:"9967f822a9b83a074e38",4572:"4bb1960b110d195d1658",4579:"16ca3c26d224ec2bea51",4625:"51252df40a568e9858e9",4662:"b32dd6447e5fae270c83",4667:"48c3843ffce6d71edad4",4732:"40416b4ab4e61de326ae",4757:"93d740911bd493adf140",4758:"139bfe0e5a3d55b967f5",4787:"c184da261d9298c6db92",4790:"03d4f572c0e1a241ad52",4794:"604a01412367c61f28d1",4797:"ec310aed295dd6ac6d3e",4810:"c9e88f8bb26309aea9a3",4817:"c6d5f79ba80cd01dc865",4832:"ef14aea5648058059b49",4851:"ddfa921c0ae9aa3cc18b",4972:"c5b4433dc989f0536983",4981:"a591e398113e3a68af10",5094:"93746d02dfb8f501e300",5181:"47ac75a7d55a7915f8bf",5201:"3ec18a3a291224aa9108",5215:"d96d8f48f1ace1189109",5224:"c47e9d538010833596c1",5226:"6827078f00442327de34",5249:"666b274dce41432ba44f",5264:"3e22171712f6f2b56160",5281:"bee09c165592668d3f89",5296:"6e8970382ccabff98a31",5330:"599272faeb108b72e7f9",5335:"8aa0878ebf5d4ad6ce59",5350:"074a558227a6662abcb5",5359:"2b8c50de5d5c4b38aca0",5367:"21ae5e3e001039f857b3",5507:"f70d497b4e7632b6cc22",5580:"24915749e40e9d761a9c",5592:"e87311d9b096af643f33",5605:"2175473641dbadf3144f",5641:"38809faee0024a508b21",5656:"75c1d98b31770205fe47",5707:"147d8ca4332836cd578d",5771:"1052f585ff4ae106bee8",5777:"554d568382eb31588d65",5802:"6cc12bb8302843f1d8f2",5816:"280673beea0b5f2fd1e1",5832:"0c735281dd62de64b370",5838:"dbba442e12c14d0a2a2e",5962:"72dc9794359fb77a60d2",5972:"19c7fc52abf01d211d54",5998:"1ee3b4651923335492d5",6061:"55bf4311a87981b3e733",6126:"91fa0738674c868ec8cc",6150:"dc68c567fc3c38729c6e",6167:"d6258818427262c45fa8",6172:"2d2ae3a66a111f064bb2",6207:"6910f3c4f0be2cfcd7f9",6254:"fb638befd53ef04822fc",6277:"9ab483681e0dd61115fd",6303:"ad52f9efd303183abf5e",6371:"83c9e45ceb3fbb5ac155",6377:"0cf4434a790b254858ca",6420:"c893ff2534f9ec304fc8",6447:"ae65f54f868cf08677c1",6486:"40ed2ed019bff637c535",6507:"45af87d3e964f08e8a6b",6668:"55647a5d1bc9e3c671d6",6682:"9becee958a13c31f4d51",6693:"a82d5d3b4ae002cead01",6758:"6fcf8c53e0a66334e5b5",6819:"e5d97b6c04bdd4635620",6839:"e28294d51df437cc6b53",6883:"520bd0ef8bbe299a89fd",6961:"d2477df2a28b8ea47ea2",6977:"d2b3c9ce6ad0030f20e0",6981:"a398d4d79a48e5730885",7183:"5a6c8f84f8386ea3c3ed",7249:"4073992e83966234ebec",7275:"7c3b58f1d8197ca0f5d1",7405:"108895750399ba59f40d",7460:"6a739700fefd3a4fbac2",7465:"e625fc96fa7fcd306780",7521:"17853734126a038a2576",7584:"f1a7f6c3be667fceb4de",7610:"fe88065240ff7a6e5504",7633:"7c65aad75c5d0729650f",7654:"1cc0055d2d390c30d171",7716:"26ccebd94ddb1fb178f8",7760:"df6139586bc8db9f4686",7803:"fa5606e48db6b49a7a94",7832:"741031b8b31f62237cd5",7850:"daed96c9f6d33ebc1f7c",7922:"5d8ea477355f17a5b790",7929:"278820dd70f564f26754",7974:"ce5288c3f1df15948dfd",7979:"fc02d437961fd476496a",7984:"9934eaf18fb03f9dfb88",8041:"f11390e201c64075fd20",8146:"023f5a9d20413b6c62d8",8174:"3c9be19d3316790eddeb",8289:"36b4c99e42d78476eb2b",8312:"65a7d4d9a4760d7a5210",8349:"7aa90fbe18ad73a1b95a",8371:"5f4cc87324b00cef7cab",8398:"602f4d50559d187c1db8",8425:"d4ab2b8d82b74d62566e",8463:"44ea1565bba7d3f2c8f7",8464:"882d97a886a01f301481",8549:"1ac42a66c2ee64bd74ec",8616:"dee76665d36ed3374636",8623:"553364f335b53f0d7c1e",8650:"67b7db5dd364cb97ebc5",8682:"689daa7df9dd2c6fa4fd",8695:"01d9bc6edddbf539b1b7",8701:"dc881152d46536521640",8750:"dc92e0e945b83ec1e05f",8774:"3a6e21ec778ef51dd932",8859:"2552cd87af4b757219b6",8883:"a09378804d20733f3763",8924:"1622880c6fb5e4f1cfe3",8970:"cc02d84919fe9ecd9cde",9013:"a4b833b1258c7c9a94fd",9049:"fc259b02f224dda0c43c",9052:"02f43b9abb68bfc5f39c",9109:"276f36aed8996da1df63",9137:"8555a9369225c49047c8",9173:"ac015221231d81f6895b",9305:"34d5c67b5c79995f8a60",9322:"b26e9b6b0c073f28a102",9325:"1defe50332e08632f07f",9393:"442f478da05ba19070c4",9396:"516ebbc17daf1bbf9ee6",9452:"e1523e3b675317504ad7",9483:"9fc1ae1899dad20e9396",9502:"d131c1c917b06c5e8366",9510:"c5c3e89e58541aa7825b",9558:"d2eaa19757d176a93ab7",9767:"ad438ca70361b5e69126",9783:"49a1c1edbc5c0821771f",9794:"c13a738c3f6b2ba76ca9",9811:"21a7c18f6923c4c737b9",9835:"2ae69e7cc7d63355340e",9857:"6a190c6f42d0d89b5004",9911:"8dd0d84bc48a0f50dd48"}[e]+".chunk.js",c.miniCssF=e=>(({452:"DashboardContainer",9502:"AlertList"}[e]||e)+"."+{380:"78b7b6dc715440560460",452:"258cd8cc24edac1875e0",1862:"8b03e8bb1c84992cbf32",1877:"e33515e5bd6542b94f77",2045:"2e374ea725d1d98f2dc1",3501:"b1f59c8250c7436d58a1",3745:"03ab023678c0223d3569",3986:"b65058c809eb4184aab8",4194:"0e16885080d878e0abd0",5605:"2175473641dbadf3144f",6172:"2d2ae3a66a111f064bb2",6277:"9ab483681e0dd61115fd",6839:"e28294d51df437cc6b53",6961:"d2477df2a28b8ea47ea2",7275:"7c3b58f1d8197ca0f5d1",7465:"e625fc96fa7fcd306780",7929:"278820dd70f564f26754",7979:"fc02d437961fd476496a",8146:"023f5a9d20413b6c62d8",8549:"1ac42a66c2ee64bd74ec",8623:"553364f335b53f0d7c1e",8650:"67b7db5dd364cb97ebc5",8859:"2552cd87af4b757219b6",9049:"fc259b02f224dda0c43c",9502:"d131c1c917b06c5e8366",9783:"49a1c1edbc5c0821771f",9835:"2ae69e7cc7d63355340e",9911:"8dd0d84bc48a0f50dd48"}[e]+".chunk.css"),c.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),c.hmd=e=>((e=Object.create(e)).children||(e.children=[]),Object.defineProperty(e,"exports",{enumerable:!0,set:()=>{throw new Error("ES Modules may not assign module.exports or exports.*, Use ESM export syntax, instead: "+e.id)}}),e),c.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),i={},n="superset:",c.l=(e,t,a,r)=>{if(i[e])i[e].push(t);else{var d,o;if(void 0!==a)for(var l=document.getElementsByTagName("script"),s=0;s<l.length;s++){var u=l[s];if(u.getAttribute("src")==e||u.getAttribute("data-webpack")==n+a){d=u;break}}d||(o=!0,(d=document.createElement("script")).charset="utf-8",d.timeout=120,c.nc&&d.setAttribute("nonce",c.nc),d.setAttribute("data-webpack",n+a),d.src=e),i[e]=[t];var b=(t,a)=>{d.onerror=d.onload=null,clearTimeout(f);var n=i[e];if(delete i[e],d.parentNode&&d.parentNode.removeChild(d),n&&n.forEach((e=>e(a))),t)return t(a)},f=setTimeout(b.bind(null,void 0,{type:"timeout",target:d}),12e4);d.onerror=b.bind(null,d.onerror),d.onload=b.bind(null,d.onload),o&&document.head.appendChild(d)}},c.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},c.nmd=e=>(e.paths=[],e.children||(e.children=[]),e),c.p="/static/assets/",r=e=>new Promise(((t,a)=>{var i=c.miniCssF(e),n=c.p+i;if(((e,t)=>{for(var a=document.getElementsByTagName("link"),i=0;i<a.length;i++){var n=(d=a[i]).getAttribute("data-href")||d.getAttribute("href");if("stylesheet"===d.rel&&(n===e||n===t))return d}var r=document.getElementsByTagName("style");for(i=0;i<r.length;i++){var d;if((n=(d=r[i]).getAttribute("data-href"))===e||n===t)return d}})(i,n))return t();((e,t,a,i)=>{var n=document.createElement("link");n.rel="stylesheet",n.type="text/css",n.onerror=n.onload=r=>{if(n.onerror=n.onload=null,"load"===r.type)a();else{var d=r&&("load"===r.type?"missing":r.type),o=r&&r.target&&r.target.href||t,l=new Error("Loading CSS chunk "+e+" failed.\n("+o+")");l.code="CSS_CHUNK_LOAD_FAILED",l.type=d,l.request=o,n.parentNode.removeChild(n),i(l)}},n.href=t,document.head.appendChild(n)})(e,n,t,a)})),d={7103:0,9783:0},c.f.miniCss=(e,t)=>{d[e]?t.push(d[e]):0!==d[e]&&{380:1,452:1,1862:1,1877:1,2045:1,3501:1,3745:1,3986:1,4194:1,5605:1,6172:1,6277:1,6839:1,6961:1,7275:1,7465:1,7929:1,7979:1,8146:1,8549:1,8623:1,8650:1,8859:1,9049:1,9502:1,9783:1,9835:1,9911:1}[e]&&t.push(d[e]=r(e).then((()=>{d[e]=0}),(t=>{throw delete d[e],t})))},(()=>{var e={7103:0,9783:0};c.f.j=(t,a)=>{var i=c.o(e,t)?e[t]:void 0;if(0!==i)if(i)a.push(i[2]);else if(/^(7275|8146|9783)$/.test(t))e[t]=0;else{var n=new Promise(((a,n)=>i=e[t]=[a,n]));a.push(i[2]=n);var r=c.p+c.u(t),d=new Error;c.l(r,(a=>{if(c.o(e,t)&&(0!==(i=e[t])&&(e[t]=void 0),i)){var n=a&&("load"===a.type?"missing":a.type),r=a&&a.target&&a.target.src;d.message="Loading chunk "+t+" failed.\n("+n+": "+r+")",d.name="ChunkLoadError",d.type=n,d.request=r,i[1](d)}}),"chunk-"+t,t)}},c.H.j=t=>{if(!(c.o(e,t)&&void 0!==e[t]||/^(7275|8146|9783)$/.test(t))){e[t]=null;var a=document.createElement("link");a.charset="utf-8",c.nc&&a.setAttribute("nonce",c.nc),a.rel="preload",a.as="script",a.href=c.p+c.u(t),document.head.appendChild(a)}},c.O.j=t=>0===e[t];var t=(t,a)=>{var i,n,[r,d,o]=a,l=0;if(r.some((t=>0!==e[t]))){for(i in d)c.o(d,i)&&(c.m[i]=d[i]);if(o)var s=o(c)}for(t&&t(a);l<r.length;l++)n=r[l],c.o(e,n)&&e[n]&&e[n][0](),e[r[l]]=0;return c.O(s)},a=globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[];a.forEach(t.bind(null,0)),a.push=t.bind(null,a.push.bind(a))})(),o={5296:[1216,995,876,2671,1163,193,4443,818,452]},c.f.preload=e=>{var t=o[e];Array.isArray(t)&&t.map(c.G)},c.O(void 0,[1216,7550,4998,2102,905,1334,9356,2717,741,5473,995,5379,571,9602,5755,9525,6962,5806,7843,1603,7727,3375,3389,6559,9152,7825,6052,818],(()=>c(85156)));var u=c.O(void 0,[1216,7550,4998,2102,905,1334,9356,2717,741,5473,995,5379,571,9602,5755,9525,6962,5806,7843,1603,7727,3375,3389,6559,9152,7825,6052,818],(()=>c(40164)));u=c.O(u)})();