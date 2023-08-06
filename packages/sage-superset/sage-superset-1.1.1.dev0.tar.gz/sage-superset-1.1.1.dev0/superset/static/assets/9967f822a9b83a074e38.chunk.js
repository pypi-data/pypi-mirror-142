"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[4502],{27989:(e,t,a)=>{a.d(t,{Z:()=>m});var l=a(67294),s=a(51995),o=a(61988),n=a(35932),r=a(74069),i=a(4715),d=a(34858),u=a(11965);const c=s.iK.div`
  display: block;
  color: ${({theme:e})=>e.colors.grayscale.base};
  font-size: ${({theme:e})=>e.typography.sizes.s-1}px;
`,p=s.iK.div`
  padding-bottom: ${({theme:e})=>2*e.gridUnit}px;
  padding-top: ${({theme:e})=>2*e.gridUnit}px;

  & > div {
    margin: ${({theme:e})=>e.gridUnit}px 0;
  }

  &.extra-container {
    padding-top: 8px;
  }

  .confirm-overwrite {
    margin-bottom: ${({theme:e})=>2*e.gridUnit}px;
  }

  .input-container {
    display: flex;
    align-items: center;

    label {
      display: flex;
      margin-right: ${({theme:e})=>2*e.gridUnit}px;
    }

    i {
      margin: 0 ${({theme:e})=>e.gridUnit}px;
    }
  }

  input,
  textarea {
    flex: 1 1 auto;
  }

  textarea {
    height: 160px;
    resize: none;
  }

  input::placeholder,
  textarea::placeholder {
    color: ${({theme:e})=>e.colors.grayscale.light1};
  }

  textarea,
  input[type='text'],
  input[type='number'] {
    padding: ${({theme:e})=>1.5*e.gridUnit}px
      ${({theme:e})=>2*e.gridUnit}px;
    border-style: none;
    border: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
    border-radius: ${({theme:e})=>e.gridUnit}px;

    &[name='name'] {
      flex: 0 1 auto;
      width: 40%;
    }

    &[name='sqlalchemy_uri'] {
      margin-right: ${({theme:e})=>3*e.gridUnit}px;
    }
  }
`,m=({resourceName:e,resourceLabel:t,passwordsNeededMessage:a,confirmOverwriteMessage:s,addDangerToast:m,onModelImport:b,show:h,onHide:g,passwordFields:Z=[],setPasswordFields:y=(()=>{})})=>{const[w,_]=(0,l.useState)(!0),[v,f]=(0,l.useState)({}),[x,S]=(0,l.useState)(!1),[C,$]=(0,l.useState)(!1),[D,k]=(0,l.useState)([]),[E,N]=(0,l.useState)(!1),T=()=>{k([]),y([]),f({}),S(!1),$(!1),N(!1)},{state:{alreadyExists:q,passwordsNeeded:H},importResource:R}=(0,d.PW)(e,t,(e=>{T(),m(e)}));(0,l.useEffect)((()=>{y(H),H.length>0&&N(!1)}),[H,y]),(0,l.useEffect)((()=>{S(q.length>0),q.length>0&&N(!1)}),[q,S]);return w&&h&&_(!1),(0,u.tZ)(r.Z,{name:"model",className:"import-model-modal",disablePrimaryButton:0===D.length||x&&!C||E,onHandledPrimaryAction:()=>{var e;(null==(e=D[0])?void 0:e.originFileObj)instanceof File&&(N(!0),R(D[0].originFileObj,v,C).then((e=>{e&&(T(),b())})))},onHide:()=>{_(!0),g(),T()},primaryButtonName:x?(0,o.t)("Overwrite"):(0,o.t)("Import"),primaryButtonType:x?"danger":"primary",width:"750px",show:h,title:(0,u.tZ)("h4",null,(0,o.t)("Import %s",t))},(0,u.tZ)(p,null,(0,u.tZ)(i.gq,{name:"modelFile",id:"modelFile",accept:".yaml,.json,.yml,.zip",fileList:D,onChange:e=>{k([{...e.file,status:"done"}])},onRemove:e=>(k(D.filter((t=>t.uid!==e.uid))),!1),customRequest:()=>{}},(0,u.tZ)(n.Z,{loading:E},"Select file"))),0===Z.length?null:(0,u.tZ)(l.Fragment,null,(0,u.tZ)("h5",null,"Database passwords"),(0,u.tZ)(c,null,a),Z.map((e=>(0,u.tZ)(p,{key:`password-for-${e}`},(0,u.tZ)("div",{className:"control-label"},e,(0,u.tZ)("span",{className:"required"},"*")),(0,u.tZ)("input",{name:`password-${e}`,autoComplete:`password-${e}`,type:"password",value:v[e],onChange:t=>f({...v,[e]:t.target.value})}))))),x?(0,u.tZ)(l.Fragment,null,(0,u.tZ)(p,null,(0,u.tZ)("div",{className:"confirm-overwrite"},s),(0,u.tZ)("div",{className:"control-label"},(0,o.t)('Type "%s" to confirm',(0,o.t)("OVERWRITE"))),(0,u.tZ)("input",{id:"overwrite",type:"text",onChange:e=>{var t,a;const l=null!=(t=null==(a=e.currentTarget)?void 0:a.value)?t:"";$(l.toUpperCase()===(0,o.t)("OVERWRITE"))}}))):null)}},95413:(e,t,a)=>{a.d(t,{Y:()=>s});var l=a(61988);const s={name:(0,l.t)("Data"),tabs:[{name:"Databases",label:(0,l.t)("Databases"),url:"/databaseview/list/",usesRouter:!0},{name:"Datasets",label:(0,l.t)("Datasets"),url:"/tablemodelview/list/",usesRouter:!0},{name:"Saved queries",label:(0,l.t)("Saved queries"),url:"/savedqueryview/list/",usesRouter:!0},{name:"Query history",label:(0,l.t)("Query history"),url:"/superset/sqllab/history/",usesRouter:!0}]}},30075:(e,t,a)=>{a.r(t),a.d(t,{default:()=>E});var l=a(61988),s=a(51995),o=a(31069),n=a(67294),r=a(38703),i=a(91877),d=a(93185),u=a(34858),c=a(40768),p=a(14114),m=a(20755),b=a(17198),h=a(58593),g=a(70163),Z=a(98289),y=a(95413),w=a(27989),_=a(32228),v=a(6238),f=a(11965);const x=(0,l.t)('The passwords for the databases below are needed in order to import them. Please note that the "Secure Extra" and "Certificate" sections of the database configuration are not present in export files, and should be added manually after the import if they are needed.'),S=(0,l.t)("You are importing one or more databases that already exist. Overwriting might cause you to lose some of your work. Are you sure you want to overwrite?"),C=(0,s.iK)(g.Z.Check)`
  color: ${({theme:e})=>e.colors.grayscale.dark1};
`,$=(0,s.iK)(g.Z.CancelX)`
  color: ${({theme:e})=>e.colors.grayscale.dark1};
`,D=s.iK.div`
  color: ${({theme:e})=>e.colors.grayscale.base};

  .action-button {
    display: inline-block;
    height: 100%;
  }
`;function k({value:e}){return e?(0,f.tZ)(C,null):(0,f.tZ)($,null)}const E=(0,p.Z)((function({addDangerToast:e,addSuccessToast:t}){const{state:{loading:a,resourceCount:s,resourceCollection:p},hasPerm:C,fetchData:$,refreshData:E}=(0,u.Yi)("database",(0,l.t)("database"),e),[N,T]=(0,n.useState)(!1),[q,H]=(0,n.useState)(null),[R,z]=(0,n.useState)(null),[O,A]=(0,n.useState)(!1),[I,F]=(0,n.useState)([]),[L,U]=(0,n.useState)(!1);function M({database:e=null,modalOpen:t=!1}={}){z(e),T(t)}const P=C("can_write"),B=C("can_write"),Q=C("can_write"),j=C("can_export")&&(0,i.cr)(d.T.VERSIONED_EXPORT),Y={activeChild:"Databases",...y.Y};P&&(Y.buttons=[{"data-test":"btn-create-database",name:(0,f.tZ)(n.Fragment,null,(0,f.tZ)("i",{className:"fa fa-plus"})," ",(0,l.t)("Database")," "),buttonStyle:"primary",onClick:()=>{M({modalOpen:!0})}}],(0,i.cr)(d.T.VERSIONED_EXPORT)&&Y.buttons.push({name:(0,f.tZ)(h.u,{id:"import-tooltip",title:(0,l.t)("Import databases"),placement:"bottomRight"},(0,f.tZ)(g.Z.Import,null)),buttonStyle:"link",onClick:()=>{A(!0)}}));const K=(0,n.useMemo)((()=>[{accessor:"database_name",Header:(0,l.t)("Database")},{accessor:"backend",Header:(0,l.t)("Backend"),size:"lg",disableSortBy:!0},{accessor:"allow_run_async",Header:(0,f.tZ)(h.u,{id:"allow-run-async-header-tooltip",title:(0,l.t)("Asynchronous query execution"),placement:"top"},(0,f.tZ)("span",null,(0,l.t)("AQE"))),Cell:({row:{original:{allow_run_async:e}}})=>(0,f.tZ)(k,{value:e}),size:"sm"},{accessor:"allow_dml",Header:(0,f.tZ)(h.u,{id:"allow-dml-header-tooltip",title:(0,l.t)("Allow data manipulation language"),placement:"top"},(0,f.tZ)("span",null,(0,l.t)("DML"))),Cell:({row:{original:{allow_dml:e}}})=>(0,f.tZ)(k,{value:e}),size:"sm"},{accessor:"allow_file_upload",Header:(0,l.t)("CSV upload"),Cell:({row:{original:{allow_file_upload:e}}})=>(0,f.tZ)(k,{value:e}),size:"md"},{accessor:"expose_in_sqllab",Header:(0,l.t)("Expose in SQL Lab"),Cell:({row:{original:{expose_in_sqllab:e}}})=>(0,f.tZ)(k,{value:e}),size:"md"},{accessor:"created_by",disableSortBy:!0,Header:(0,l.t)("Created by"),Cell:({row:{original:{created_by:e}}})=>e?`${e.first_name} ${e.last_name}`:"",size:"xl"},{Cell:({row:{original:{changed_on_delta_humanized:e}}})=>e,Header:(0,l.t)("Last modified"),accessor:"changed_on_delta_humanized",size:"xl"},{Cell:({row:{original:e}})=>B||Q||j?(0,f.tZ)(D,{className:"actions"},Q&&(0,f.tZ)("span",{role:"button",tabIndex:0,className:"action-button",onClick:()=>{return t=e,o.Z.get({endpoint:`/api/v1/database/${t.id}/related_objects/`}).then((({json:e={}})=>{H({...t,chart_count:e.charts.count,dashboard_count:e.dashboards.count,sqllab_tab_count:e.sqllab_tab_states.count})})).catch((0,c.v$)((e=>(0,l.t)("An error occurred while fetching database related data: %s",e))));var t}},(0,f.tZ)(h.u,{id:"delete-action-tooltip",title:(0,l.t)("Delete database"),placement:"bottom"},(0,f.tZ)(g.Z.Trash,null))),j&&(0,f.tZ)(h.u,{id:"export-action-tooltip",title:(0,l.t)("Export"),placement:"bottom"},(0,f.tZ)("span",{role:"button",tabIndex:0,className:"action-button",onClick:()=>{var t;void 0!==(t=e).id&&((0,_.Z)("database",[t.id],(()=>{U(!1)})),U(!0))}},(0,f.tZ)(g.Z.Share,null))),B&&(0,f.tZ)(h.u,{id:"edit-action-tooltip",title:(0,l.t)("Edit"),placement:"bottom"},(0,f.tZ)("span",{role:"button",tabIndex:0,className:"action-button",onClick:()=>M({database:e,modalOpen:!0})},(0,f.tZ)(g.Z.EditAlt,null)))):null,Header:(0,l.t)("Actions"),id:"actions",hidden:!B&&!Q,disableSortBy:!0}]),[Q,B,j]),V=(0,n.useMemo)((()=>[{Header:(0,l.t)("Expose in SQL Lab"),id:"expose_in_sqllab",input:"select",operator:Z.p.equals,unfilteredLabel:"All",selects:[{label:"Yes",value:!0},{label:"No",value:!1}]},{Header:(0,f.tZ)(h.u,{id:"allow-run-async-filter-header-tooltip",title:(0,l.t)("Asynchronous query execution"),placement:"top"},(0,f.tZ)("span",null,(0,l.t)("AQE"))),id:"allow_run_async",input:"select",operator:Z.p.equals,unfilteredLabel:"All",selects:[{label:"Yes",value:!0},{label:"No",value:!1}]},{Header:(0,l.t)("Search"),id:"database_name",input:"search",operator:Z.p.contains}]),[]);return(0,f.tZ)(n.Fragment,null,(0,f.tZ)(m.Z,Y),(0,f.tZ)(v.Z,{databaseId:null==R?void 0:R.id,show:N,onHide:M,onDatabaseAdd:()=>{E()}}),q&&(0,f.tZ)(b.Z,{description:(0,l.t)("The database %s is linked to %s charts that appear on %s dashboards and users have %s SQL Lab tabs using this database open. Are you sure you want to continue? Deleting the database will break those objects.",q.database_name,q.chart_count,q.dashboard_count,q.sqllab_tab_count),onConfirm:()=>{q&&function({id:a,database_name:s}){o.Z.delete({endpoint:`/api/v1/database/${a}`}).then((()=>{E(),t((0,l.t)("Deleted: %s",s)),H(null)}),(0,c.v$)((t=>e((0,l.t)("There was an issue deleting %s: %s",s,t)))))}(q)},onHide:()=>H(null),open:!0,title:(0,l.t)("Delete Database?")}),(0,f.tZ)(Z.Z,{className:"database-list-view",columns:K,count:s,data:p,fetchData:$,filters:V,initialSort:[{id:"changed_on_delta_humanized",desc:!0}],loading:a,pageSize:25}),(0,f.tZ)(w.Z,{resourceName:"database",resourceLabel:(0,l.t)("database"),passwordsNeededMessage:x,confirmOverwriteMessage:S,addDangerToast:e,addSuccessToast:t,onModelImport:()=>{A(!1),E(),t((0,l.t)("Database imported"))},show:O,onHide:()=>{A(!1)},passwordFields:I,setPasswordFields:F}),L&&(0,f.tZ)(r.Z,null))}))}}]);