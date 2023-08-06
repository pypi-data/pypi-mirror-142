"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[5296],{81788:(t,e,o)=>{o.d(e,{TZ:()=>i,u7:()=>s,B8:()=>l});var r=o(31069),n=o(68492);const a=(t,e,o)=>{let r=`api/v1/dashboard/${t}/filter_state`;return e&&(r=r.concat(`/${e}`)),o&&(r=r.concat(`?tab_id=${o}`)),r},i=(t,e,o,i)=>r.Z.put({endpoint:a(t,o,i),jsonPayload:{value:e}}).then((t=>t.json.message)).catch((t=>(n.Z.error(t),null))),s=(t,e,o)=>r.Z.post({endpoint:a(t,void 0,o),jsonPayload:{value:e}}).then((t=>t.json.key)).catch((t=>(n.Z.error(t),null))),l=(t,e)=>r.Z.get({endpoint:a(t,e)}).then((({json:t})=>JSON.parse(t.value))).catch((t=>(n.Z.error(t),null)))},37936:(t,e,o)=>{o.r(e),o.d(e,{MigrationContext:()=>T,default:()=>z});var r=o(67294),n=o(51995),a=o(93185),i=o(61988),s=o(37703),l=o(11965),c=o(5977),u=o(14114),d=o(38703),_=o(74069),p=o(35932);const f=(0,n.iK)(_.Z)`
  .modal-content {
    height: 900px;
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }

  .modal-header {
    flex: 0 1 auto;
  }

  .modal-body {
    flex: 1 1 auto;
    overflow: auto;
  }

  .modal-footer {
    flex: 0 1 auto;
  }

  .ant-modal-body {
    overflow: auto;
  }
`,h=({onClickReview:t,onClickSnooze:e,onHide:o,show:n,hideFooter:a=!1})=>(0,l.tZ)(f,{show:n,onHide:o,title:(0,i.t)("Ready to review filters in this dashboard?"),hideFooter:a,footer:(0,l.tZ)(r.Fragment,null,(0,l.tZ)(p.Z,{buttonSize:"small",onClick:e},(0,i.t)("Remind me in 24 hours")),(0,l.tZ)(p.Z,{buttonSize:"small",onClick:o},(0,i.t)("Cancel")),(0,l.tZ)(p.Z,{buttonSize:"small",buttonStyle:"primary",onClick:t},(0,i.t)("Start Review"))),responsive:!0},(0,l.tZ)("div",null,(0,i.t)("filter_box will be deprecated in a future version of Superset. Please replace filter_box by dashboard filter components.")));var m=o(67994),b=o(63389),v=o(50810),E=o(14505),g=o(1629),O=o(72570),y=o(61337),S=o(69856),Z=o(27600),w=o(23525),x=o(70695),R=o(52794),D=o(81788);const N=t=>l.iv`
  .filter-card-popover {
    width: 240px;
    padding: 0;
    border-radius: 4px;

    .ant-popover-inner {
      box-shadow: 0 0 8px rgb(0 0 0 / 10%);
    }
    .ant-popover-inner-content {
      padding: ${4*t.gridUnit}px;
    }

    .ant-popover-arrow {
      display: none;
    }
  }

  .filter-card-tooltip {
    &.ant-tooltip-placement-bottom {
      padding-top: 0;
      & .ant-tooltip-arrow {
        top: -13px;
      }
    }
  }
`,T=r.createContext(S.Qi.NOOP);(0,g.Z)();const C=r.lazy((()=>Promise.all([o.e(1216),o.e(995),o.e(876),o.e(2671),o.e(1163),o.e(193),o.e(4443),o.e(818),o.e(452)]).then(o.bind(o,75499)))),I=document.title,z=()=>{const t=(0,s.I0)(),e=(0,n.Fg)(),o=(0,s.v9)((t=>t.user)),{addDangerToast:_}=(0,u.e)(),{idOrSlug:p}=(0,c.UO)(),{result:f,error:g}=(0,m.QU)(p),{result:z,error:k}=(0,m.Es)(p),{result:L,error:F}=(0,m.JL)(p),Q=(0,r.useRef)(!1),P=g||k,$=Boolean(f&&z),j=(0,w.e)(Z.KD.migrationState),A=(0,a.c)(a.T.ENABLE_FILTER_BOX_MIGRATION),{dashboard_title:B,css:M,metadata:H,id:J=0}=f||{},[V,U]=(0,r.useState)(j||S.Qi.NOOP);if((0,r.useEffect)((()=>{const e=z&&z.some((t=>{var e;return"filter_box"===(null==(e=t.form_data)?void 0:e.viz_type)}));if(f&&(0,x.M)(f,o)){if(null!=H&&H.native_filter_configuration)return void U(A?S.Qi.CONVERTED:S.Qi.NOOP);if(e)if(A){if(j&&Object.values(S.Qi).includes(j))return void U(j);const t=(0,y.rV)(y.dR.filter_box_transition_snoozed_at,{});if(Date.now()-(t[J]||0)<S.Yd)return void U(S.Qi.SNOOZED);U(S.Qi.UNDECIDED)}else(0,a.c)(a.T.DASHBOARD_NATIVE_FILTERS)&&t((0,O.Dz)((0,i.t)("filter_box will be deprecated in a future version of Superset. Please replace filter_box by dashboard filter components.")))}}),[$]),(0,r.useEffect)((()=>{J&&async function(){const e=(0,w.e)(Z.KD.nativeFiltersKey);let o=e||{};const r=(0,w.e)(Z.KD.nativeFilters);e&&(o=await(0,D.B8)(J,e)),r&&(o=r),$&&(Q.current||(Q.current=!0,(0,a.c)(a.T.DASHBOARD_NATIVE_FILTERS_SET)&&t((0,R.pi)(J))),t((0,b.Y)(f,z,V,o)))}()}),[$,V]),(0,r.useEffect)((()=>(B&&(document.title=B),()=>{document.title=I})),[B]),(0,r.useEffect)((()=>M?(0,E.Z)(M):()=>{}),[M]),(0,r.useEffect)((()=>{F?_((0,i.t)("Error loading chart datasources. Filters may not work correctly.")):t((0,v.Fy)(L))}),[_,L,F,t]),P)throw P;return $?(0,l.tZ)(r.Fragment,null,(0,l.tZ)(l.xB,{styles:N(e)}),(0,l.tZ)(h,{show:V===S.Qi.UNDECIDED,hideFooter:!A,onHide:()=>{U(S.Qi.SNOOZED)},onClickReview:()=>{U(S.Qi.REVIEWING)},onClickSnooze:()=>{const t=(0,y.rV)(y.dR.filter_box_transition_snoozed_at,{});(0,y.LS)(y.dR.filter_box_transition_snoozed_at,{...t,[J]:Date.now()}),U(S.Qi.SNOOZED)}}),(0,l.tZ)(T.Provider,{value:V},(0,l.tZ)(C,null))):(0,l.tZ)(d.Z,null)}},14505:(t,e,o)=>{function r(t){const e="CssEditor-css",o=document.head||document.getElementsByTagName("head")[0],r=document.querySelector(`.${e}`)||function(t){const e=document.createElement("style");return e.className="CssEditor-css",e.type="text/css",e}();return"styleSheet"in r?r.styleSheet.cssText=t:r.innerHTML=t,o.appendChild(r),function(){r.remove()}}o.d(e,{Z:()=>r})},67994:(t,e,o)=>{o.d(e,{hb:()=>p,QU:()=>f,Es:()=>h,JL:()=>m});var r,n=o(22102),a=o(67294);!function(t){t.LOADING="loading",t.COMPLETE="complete",t.ERROR="error"}(r||(r={}));const i={status:r.LOADING,result:null,error:null};function s(t,e){return(0,a.useMemo)((()=>{if(t.status!==r.COMPLETE)return t;try{return{...t,result:e(t.result)}}catch(t){return{status:r.ERROR,result:null,error:t}}}),[t,e])}const l=t=>t.result;function c(t){return s(function(t){const[e,o]=(0,a.useState)(i),s=(0,a.useRef)((()=>{}));return(0,a.useEffect)((()=>{o(i),s.current();let e=!1;return s.current=()=>{e=!0},(0,n.Z)({method:"GET",endpoint:t})({}).then((t=>{e||o({status:r.COMPLETE,result:t,error:null})})).catch((t=>{e||o({status:r.ERROR,result:null,error:t})})),()=>{e=!0}}),[t]),e}(t),l)}var u=o(15926);function d({owners:t}){return t?t.map((t=>`${t.first_name} ${t.last_name}`)):null}const _=o.n(u)().encode({columns:["owners.first_name","owners.last_name"],keys:["none"]});function p(t){return s(c(`/api/v1/chart/${t}?q=${_}`),d)}const f=t=>s(c(`/api/v1/dashboard/${t}`),(t=>({...t,metadata:t.json_metadata&&JSON.parse(t.json_metadata)||{},position_data:t.position_json&&JSON.parse(t.position_json)}))),h=t=>c(`/api/v1/dashboard/${t}/charts`),m=t=>c(`/api/v1/dashboard/${t}/datasets`)},61337:(t,e,o)=>{var r;function n(t,e){return i(t,e)}function a(t,e){s(t,e)}function i(t,e){try{const o=localStorage.getItem(t);return null===o?e:JSON.parse(o)}catch{return e}}function s(t,e){try{localStorage.setItem(t,JSON.stringify(e))}catch{}}o.d(e,{dR:()=>r,rV:()=>n,LS:()=>a,OH:()=>i,I_:()=>s}),function(t){t.filter_box_transition_snoozed_at="filter_box_transition_snoozed_at",t.chart_split_sizes="chart_split_sizes",t.controls_width="controls_width",t.datasource_width="datasource_width",t.is_datapanel_open="is_datapanel_open",t.homepage_chart_filter="homepage_chart_filter",t.homepage_dashboard_filter="homepage_dashboard_filter",t.homepage_collapse_state="homepage_collapse_state",t.homepage_activity_filter="homepage_activity_filter",t.sqllab__is_autocomplete_enabled="sqllab__is_autocomplete_enabled",t.explore__data_table_time_formatted_columns="explore__data_table_time_formatted_columns"}(r||(r={}))}}]);