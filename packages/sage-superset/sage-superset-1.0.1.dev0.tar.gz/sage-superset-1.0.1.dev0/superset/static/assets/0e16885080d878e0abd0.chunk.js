"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[4194],{44194:(e,t,a)=>{a.r(t),a.d(t,{default:()=>J}),a(67294);var i=a(43323),s=a(51995),o=a(45697),n=a.n(o),r=a(23493),l=a.n(r),c=a(21804),h=a.n(c),m=a(15078),u=a.n(m),d=a(30381),p=a.n(d),y=a(28041),x=a.n(y),b=a(28062),g=a(67190),f=a(61988),k=a(45636),v=a(51115),A=a(40962),w=a(37731),L=a(60524),M=a(95963),C=a(83937),T=a(80221);const $=n().oneOfType([n().number,n().oneOf(["auto"])]),F=n().oneOfType([n().string,n().shape({label:n().string})]),_=n().shape({r:n().number.isRequired,g:n().number.isRequired,b:n().number.isRequired}),D=n().shape({x:n().number,y:n().number}),N=n().shape({x:n().string,y:n().number}),O=n().shape({outliers:n().arrayOf(n().number),Q1:n().number,Q2:n().number,Q3:n().number,whisker_high:n().number,whisker_low:n().number}),S=n().shape({markerLabels:n().arrayOf(n().string),markerLineLabels:n().arrayOf(n().string),markerLines:n().arrayOf(n().number),markers:n().arrayOf(n().number),measures:n().arrayOf(n().number),rangeLabels:n().arrayOf(n().string),ranges:n().arrayOf(n().number)}),E=n().shape({annotationType:n().oneOf(Object.keys(M.DT)),color:n().string,hideLine:n().bool,name:n().string,opacity:n().string,show:n().bool,showMarkers:n().bool,sourceType:n().string,style:n().string,value:n().oneOfType([n().number,n().string]),width:n().number}),B=[{text:"No data",dy:"-.75em",class:"header"},{text:"Adjust filters or check the Datasource.",dy:".75em",class:"body"}];x().utils.noData=function(e,t){const a=e.options().margin(),i=x().utils.availableHeight(null,t,a),s=x().utils.availableWidth(null,t,a),o=a.left+s/2,n=a.top+i/2;t.selectAll("g").remove();const r=t.selectAll(".nv-noData").data(B);r.enter().append("text").attr("class",(e=>`nvd3 nv-noData ${e.class}`)).attr("dy",(e=>e.dy)).style("text-anchor","middle"),r.attr("x",o).attr("y",n).text((e=>e.text))};const{getColor:z,getScale:R}=b,G=["line","dual_line","line_multi","area","compare","bar","time_pivot"],Z={data:n().oneOfType([n().arrayOf(n().oneOfType([N,n().shape({key:n().string,values:n().arrayOf(N)}),n().shape({key:n().arrayOf(n().string),values:n().arrayOf(D)}),n().shape({classed:n().string,key:n().string,type:n().string,values:n().arrayOf(D),yAxis:n().number}),n().shape({label:n().string,values:n().arrayOf(O)}),n().shape({key:n().string,values:n().arrayOf(n().object)})])),S]),width:n().number,height:n().number,annotationData:n().object,annotationLayers:n().arrayOf(E),bottomMargin:$,colorScheme:n().string,comparisonType:n().string,contribution:n().bool,leftMargin:$,onError:n().func,showLegend:n().bool,showMarkers:n().bool,useRichTooltip:n().bool,vizType:n().oneOf(["area","bar","box_plot","bubble","bullet","compare","column","dist_bar","line","line_multi","time_pivot","pie","dual_line"]),xAxisFormat:n().string,numberFormat:n().string,xAxisLabel:n().string,xAxisShowMinMax:n().bool,xIsLogScale:n().bool,xTicksLayout:n().oneOf(["auto","staggered","45°"]),yAxisFormat:n().string,yAxisBounds:n().arrayOf(n().number),yAxisLabel:n().string,yAxisShowMinMax:n().bool,yIsLogScale:n().bool,orderBars:n().bool,isBarStacked:n().bool,showBarValue:n().bool,reduceXTicks:n().bool,showControls:n().bool,showBrush:n().oneOf([!0,"yes",!1,"no","auto"]),onBrushEnd:n().func,yAxis2Format:n().string,lineInterpolation:n().string,isDonut:n().bool,isPieLabelOutside:n().bool,pieLabelType:n().oneOf(["key","value","percent","key_value","key_percent","key_value_percent"]),showLabels:n().bool,areaStackedStyle:n().string,entity:n().string,maxBubbleSize:n().number,xField:F,yField:F,sizeField:F,baseColor:_},I=()=>{},P=(0,g.JB)();function V(e,t){const{data:a,width:i,height:s,annotationData:o,annotationLayers:n=[],areaStackedStyle:r,baseColor:c,bottomMargin:m,colorScheme:d,comparisonType:y,contribution:b,entity:$,isBarStacked:F,isDonut:_,isPieLabelOutside:D,leftMargin:N,lineInterpolation:O="linear",markerLabels:S,markerLines:E,markerLineLabels:B,markers:Z,maxBubbleSize:V,onBrushEnd:U=I,onError:W=I,orderBars:H,pieLabelType:q,rangeLabels:J,ranges:j,reduceXTicks:X=!1,showBarValue:Q,showBrush:Y,showControls:K,showLabels:ee,showLegend:te,showMarkers:ae,sizeField:ie,useRichTooltip:se,vizType:oe,xAxisFormat:ne,numberFormat:re,xAxisLabel:le,xAxisShowMinMax:ce=!1,xField:he,xIsLogScale:me,xTicksLayout:ue,yAxisFormat:de,yAxis2Format:pe,yAxisBounds:ye,yAxis2Bounds:xe,yAxisLabel:be,yAxisShowMinMax:ge=!1,yAxis2ShowMinMax:fe=!1,yField:ke,yIsLogScale:ve}=t,Ae=null!==document.querySelector("#explorer-container"),we=e;we.innerHTML="";const Le=n.filter((e=>e.show));let Me,Ce=we,Te=null;for(;Ce.parentElement;){if(Ce.parentElement.id.startsWith("chart-id-")){Te=Ce.parentElement.id;break}Ce=Ce.parentElement}let $e=i,Fe="key";function _e(e){return e.includes(oe)}we.style.width=`${i}px`,we.style.height=`${s}px`,Te?(0,T.o2)(Te):(0,T.Vl)(!0),x().addGraph((function(){const t=u().select(e);t.classed("superset-legacy-chart-nvd3",!0),t.classed(`superset-legacy-chart-nvd3-${h()(oe)}`,!0);let n=t.select("svg");n.empty()&&(n=t.append("svg"));const we="bullet"===oe?Math.min(s,50):s,Ce=_e(G),De="staggered"===ue,Ne="auto"===ue&&_e(["column","dist_bar"])||"45°"===ue?45:0;if(45===Ne&&(0,C.Z)(Y))return W((0,f.t)("You cannot use 45° tick layout along with the time range filter")),null;const Oe=(0,C.Z)(Y)||"auto"===Y&&s>=480&&"45°"!==ue,Se=(0,g.JB)(re);switch(oe){case"line":Oe?(Me=x().models.lineWithFocusChart(),De&&(Me.focus.margin({bottom:40}),Me.focusHeight(80)),Me.focus.xScale(u().time.scale.utc())):Me=x().models.lineChart(),Me.xScale(u().time.scale.utc()),Me.interpolate(O),Me.clipEdge(!1);break;case"time_pivot":Me=x().models.lineChart(),Me.xScale(u().time.scale.utc()),Me.interpolate(O);break;case"dual_line":case"line_multi":Me=x().models.multiChart(),Me.interpolate(O),Me.xScale(u().time.scale.utc());break;case"bar":Me=x().models.multiBarChart().showControls(K).groupSpacing(.1),X||($e=(0,T.UG)(a,F,i)),Me.width($e),Me.xAxis.showMaxMin(!1),Me.stacked(F);break;case"dist_bar":Me=x().models.multiBarChart().showControls(K).reduceXTicks(X).groupSpacing(.1),Me.xAxis.showMaxMin(!1),Me.stacked(F),H&&a.forEach((e=>{e.values.sort(((e,t)=>(0,T.Hy)(e.x)<(0,T.Hy)(t.x)?-1:1))})),X||($e=(0,T.UG)(a,F,i)),Me.width($e);break;case"pie":if(Me=x().models.pieChart(),Fe="x",Me.valueFormat(Se),_&&Me.donut(!0),Me.showLabels(ee),Me.labelsOutside(D),Me.labelThreshold(.05),Me.cornerRadius(!0),["key","value","percent"].includes(q))Me.labelType(q);else if("key_value"===q)Me.labelType((e=>`${e.data.x}: ${Se(e.data.y)}`));else{const e=u().sum(a,(e=>e.y)),t=(0,g.JB)(k.Z.PERCENT_2_POINT);"key_percent"===q?(Me.tooltip.valueFormatter((e=>t(e))),Me.labelType((a=>`${a.data.x}: ${t(a.data.y/e)}`))):(Me.tooltip.valueFormatter((a=>`${Se(a)} (${t(a/e)})`)),Me.labelType((a=>`${a.data.x}: ${Se(a.data.y)} (${t(a.data.y/e)})`)))}Me.margin({top:0});break;case"column":Me=x().models.multiBarChart().reduceXTicks(!1);break;case"compare":Me=x().models.cumulativeLineChart(),Me.xScale(u().time.scale.utc()),Me.useInteractiveGuideline(!0),Me.xAxis.showMaxMin(!1);break;case"bubble":Me=x().models.scatterChart(),Me.showDistX(!1),Me.showDistY(!1),Me.tooltip.contentGenerator((e=>(0,T.zK)({point:e.point,entity:$,xField:he,yField:ke,sizeField:ie,xFormatter:(0,T.fF)(ne),yFormatter:(0,T.fF)(de),sizeFormatter:P}))),Me.pointRange([5,V**2]),Me.pointDomain([0,u().max(a,(e=>u().max(e.values,(e=>e.size))))]);break;case"area":Me=x().models.stackedAreaChart(),Me.showControls(K),Me.style(r),Me.xScale(u().time.scale.utc());break;case"box_plot":Fe="label",Me=x().models.boxPlotChart(),Me.x((e=>e.label)),Me.maxBoxWidth(75);break;case"bullet":Me=x().models.bulletChart(),a.rangeLabels=J,a.ranges=j,a.markerLabels=S,a.markerLines=E,a.markerLineLabels=B,a.markers=Z;break;default:throw new Error(`Unrecognized visualization for nvd3${oe}`)}let Ee;Me.margin({left:0,bottom:0}),Q&&((0,T.Ad)(n,a,F,de),Me.dispatch.on("stateChange.drawBarValues",(()=>{(0,T.Ad)(n,a,F,de)}))),Oe&&U!==I&&Me.focus&&Me.focus.dispatch.on("brush",(e=>{const t=(0,T.z_)(e.extent);t&&e.brush.on("brushend",(()=>{U(t)}))})),Me.xAxis&&Me.xAxis.staggerLabels&&Me.xAxis.staggerLabels(De),Me.xAxis&&Me.xAxis.rotateLabels&&Me.xAxis.rotateLabels(Ne),Me.x2Axis&&Me.x2Axis.staggerLabels&&Me.x2Axis.staggerLabels(De),Me.x2Axis&&Me.x2Axis.rotateLabels&&Me.x2Axis.rotateLabels(Ne),"showLegend"in Me&&void 0!==te&&($e<340&&"pie"!==oe?Me.showLegend(!1):Me.showLegend(te)),ve&&Me.yScale(u().scale.log()),me&&Me.xScale(u().scale.log()),Ce?(Ee=(0,v.bt)(ne),Me.interactiveLayer.tooltip.headerFormatter(A.Z)):Ee=(0,T.fF)(ne),Me.x2Axis&&Me.x2Axis.tickFormat&&Me.x2Axis.tickFormat(Ee),Me.xAxis&&Me.xAxis.tickFormat&&(_e(["dist_bar","box_plot"])?Me.xAxis.tickFormat((e=>e.length>40?`${e.slice(0,Math.max(0,40))}…`:e)):Me.xAxis.tickFormat(Ee));let Be=(0,T.fF)(de);if(Me.yAxis&&Me.yAxis.tickFormat&&(!b&&"percentage"!==y||de&&de!==k.Z.SMART_NUMBER&&de!==k.Z.SMART_NUMBER_SIGNED||(Be=(0,g.JB)(k.Z.PERCENT_1_POINT)),Me.yAxis.tickFormat(Be)),Me.y2Axis&&Me.y2Axis.tickFormat&&Me.y2Axis.tickFormat(Be),Me.yAxis&&Me.yAxis.ticks(5),Me.y2Axis&&Me.y2Axis.ticks(5),(0,T.Ml)(Me.xAxis,ce),(0,T.Ml)(Me.x2Axis,ce),(0,T.Ml)(Me.yAxis,ge),(0,T.Ml)(Me.y2Axis,fe||ge),"time_pivot"===oe){if(c){const{r:e,g:t,b:a}=c;Me.color((i=>{const s=i.rank>0?.5*i.perc:1;return`rgba(${e}, ${t}, ${a}, ${s})`}))}Me.useInteractiveGuideline(!0),Me.interactiveLayer.tooltip.contentGenerator((e=>(0,T.RO)(e,Ee,Be)))}else if("bullet"!==oe){const e=R(d);Me.color((t=>t.color||e((0,T.gO)(t[Fe]))))}if(_e(["line","area","bar","dist_bar"])&&se&&(Me.useInteractiveGuideline(!0),"line"===oe||"bar"===oe?Me.interactiveLayer.tooltip.contentGenerator((e=>(0,T.Gx)(e,A.Z,Be))):"dist_bar"===oe?Me.interactiveLayer.tooltip.contentGenerator((e=>(0,T.yy)(e,Be))):Me.interactiveLayer.tooltip.contentGenerator((e=>(0,T.n4)(e,A.Z,Be,Me)))),_e(["compare"])&&Me.interactiveLayer.tooltip.contentGenerator((e=>(0,T.yy)(e,Be))),_e(["dual_line","line_multi"])){const e=(0,g.JB)(de),t=(0,g.JB)(pe);Me.yAxis1.tickFormat(e),Me.yAxis2.tickFormat(t);const i=a.map((a=>1===a.yAxis?e:t));Me.useInteractiveGuideline(!0),Me.interactiveLayer.tooltip.contentGenerator((e=>(0,T.HO)(e,Ee,i)))}Me.width($e),Me.height(we),n.datum(a).transition().duration(500).attr("height",we).attr("width",$e).call(Me),ve&&Me.yAxis.tickFormat((e=>0!==e&&Math.log10(e)%1==0?Be(e):"")),Ne>0&&n.select(".nv-x.nv-axis > g").selectAll("g").selectAll("text").attr("dx",-6.5);const ze=()=>{if(Me.yDomain&&Array.isArray(ye)&&2===ye.length){const[e,t]=ye,i=(0,w.Z)(e)&&!Number.isNaN(e),s=(0,w.Z)(t)&&!Number.isNaN(t);if((i||s)&&"area"===oe&&"expand"===Me.style())Me.yDomain([0,1]);else if((i||s)&&"area"===oe&&"stream"===Me.style())Me.yDomain((0,T.po)(a));else if(i&&s)Me.yDomain([e,t]),Me.clipEdge(!0);else if(i||s){let[o,n]=[0,1];"area"===oe||_e(["bar","dist_bar"])&&Me.stacked()?[o,n]=(0,T.po)(a):[o,n]=(0,T.tH)(a);const r=i?e:o,l=s?t:n;Me.yDomain([r,l]),Me.clipEdge(!0)}}};if(ze(),Me.dispatch&&Me.dispatch.stateChange&&Me.dispatch.on("stateChange.applyYAxisBounds",ze),_e(["dual_line","line_multi"])){const e=Me.yAxis1.ticks(),t=Me.yAxis1.scale().domain(Me.yAxis1.domain()).nice(e).ticks(e),a=Me.yAxis2.scale().domain(Me.yAxis2.domain()).nice(e).ticks(e),i=t.length-a.length;if(t.length>0&&a.length>0&&0!==i){const e=i<0?t:a,s=e[1]-e[0];for(let t=0;t<Math.abs(i);t+=1)t%2==0?e.unshift(e[0]-s):e.push(e[e.length-1]+s);Me.yDomain1([t[0],t[t.length-1]]),Me.yDomain2([a[0],a[a.length-1]]),Me.yAxis1.tickValues(t),Me.yAxis2.tickValues(a)}Me.yDomain1([ye[0]||t[0],ye[1]||t[t.length-1]]),Me.yDomain2([xe[0]||a[0],xe[1]||a[a.length-1]])}if(ae&&(n.selectAll(".nv-point").style("stroke-opacity",1).style("fill-opacity",1),Me.dispatch.on("stateChange.showMarkers",(()=>{setTimeout((()=>{n.selectAll(".nv-point").style("stroke-opacity",1).style("fill-opacity",1)}),10)}))),void 0!==Me.yAxis||void 0!==Me.yAxis2){const t=Math.ceil(Math.min(i*(Ae?.01:.03),30)),s=Me.margin();Me.xAxis&&(s.bottom=28);const r=(0,T.GF)(n,Me.yAxis2?"nv-y1":"nv-y"),c=(0,T.GF)(n,"nv-x");if(s.left=r+t,be&&""!==be&&(s.left+=25),Q&&(s.top+=24),ce&&(s.right=Math.max(20,c/2)+t),45===Ne?(s.bottom=c*Math.sin(Math.PI*Ne/180)+t+30,s.right=c*Math.cos(Math.PI*Ne/180)+t):De&&(s.bottom=40),_e(["dual_line","line_multi"])){const e=(0,T.GF)(n,"nv-y2");s.right=e+t}if(m&&"auto"!==m&&(s.bottom=parseInt(m,10)),N&&"auto"!==N&&(s.left=N),le&&""!==le&&Me.xAxis){s.bottom+=25;let e=0;s.bottom&&!Number.isNaN(s.bottom)&&(e=s.bottom-45),Me.xAxis.axisLabel(le).axisLabelDistance(e)}if(be&&""!==be&&Me.yAxis){let e=0;s.left&&!Number.isNaN(s.left)&&(e=s.left-70),Me.yAxis.axisLabel(be).axisLabelDistance(e)}if(Ce&&o&&Le.length>0){const e=Le.filter((e=>e.annotationType===M.ZP.TIME_SERIES)).reduce(((e,t)=>e.concat((o[t.name]||[]).map((e=>{if(!e)return{};const a=Array.isArray(e.key)?`${t.name}, ${e.key.join(", ")}`:`${t.name}, ${e.key}`;return{...e,key:a,color:t.color,strokeWidth:t.width,classed:`${t.opacity} ${t.style} nv-timeseries-annotation-layer showMarkers${t.showMarkers} hideLine${t.hideLine}`}})))),[]);a.push(...e)}if(Te&&(Me&&Me.interactiveLayer&&Me.interactiveLayer.tooltip&&Me.interactiveLayer.tooltip.classes([(0,T.T7)(Te)]),Me&&Me.tooltip&&Me.tooltip.classes([(0,T.T7)(Te)])),Me.margin(s),n.datum(a).transition().duration(500).attr("width",$e).attr("height",we).call(Me),window.addEventListener("scroll",l()((()=>(0,T.Vl)(!1)),250)),Ce&&Le.length>0){const t=Le.filter((e=>e.annotationType===M.ZP.FORMULA));let i,s,r;if("bar"===oe?(s=u().min(a[0].values,(e=>e.x)),i=u().max(a[0].values,(e=>e.x)),r=u().scale.quantile().domain([s,i]).range(Me.xAxis.range())):(s=Me.xAxis.scale().domain()[0].valueOf(),i=Me.xAxis.scale().domain()[1].valueOf(),r=Me.xScale?Me.xScale():Me.xAxis.scale?Me.xAxis.scale():u().scale.linear()),r&&r.clamp&&r.clamp(!0),t.length>0){const e=[];if("bar"===oe){const t=a.reduce(((e,t)=>(t.values.forEach((t=>e.add(t.x))),e)),new Set);e.push(...t.values()),e.sort()}else{let t=Math.min(...a.map((e=>Math.min(...e.values.slice(1).map(((t,a)=>t.x-e.values[a].x))))));const o=(i-s)/(t||1);t=o<100?(i-s)/100:t,t=o>500?(i-s)/500:t,e.push(s);for(let a=s;a<i;a+=t)e.push(a);e.push(i)}const o=t.map((t=>{const{value:a}=t;return{key:t.name,values:e.map((e=>({x:e,y:(0,L.f)(a,e)}))),color:t.color,strokeWidth:t.width,classed:`${t.opacity} ${t.style}`}}));a.push(...o)}const l=Me.xAxis1?Me.xAxis1:Me.xAxis,c=Me.yAxis1?Me.yAxis1:Me.yAxis,h=l.scale().range()[1],m=c.scale().range()[0];o&&(Le.filter((e=>e.annotationType===M.ZP.EVENT&&o&&o[e.name])).forEach(((t,a)=>{const i=(0,M.yb)(t),s=u().select(e).select(".nv-wrap").append("g").attr("class",`nv-event-annotation-layer-${a}`),n=i.color||z((0,T.gO)(i.name),d),l=(0,T.Gr)({...i,annotationTipClass:`arrow-down nv-event-annotation-layer-${t.sourceType}`}),c=(o[i.name].records||[]).map((e=>{const t=new Date(p().utc(e[i.timeColumn]));return{...e,[i.timeColumn]:t}})).filter((e=>!Number.isNaN(e[i.timeColumn].getMilliseconds())));c.length>0&&s.selectAll("line").data(c).enter().append("line").attr({x1:e=>r(new Date(e[i.timeColumn])),y1:0,x2:e=>r(new Date(e[i.timeColumn])),y2:m}).attr("class",`${i.opacity} ${i.style}`).style("stroke",n).style("stroke-width",i.width).on("mouseover",l.show).on("mouseout",l.hide).call(l),Me.focus&&Me.focus.dispatch.on("onBrush.event-annotation",(()=>{s.selectAll("line").data(c).attr({x1:e=>r(new Date(e[i.timeColumn])),y1:0,x2:e=>r(new Date(e[i.timeColumn])),y2:m,opacity:e=>{const t=r(new Date(e[i.timeColumn]));return t>0&&t<h?1:0}})}))})),Le.filter((e=>e.annotationType===M.ZP.INTERVAL&&o&&o[e.name])).forEach(((t,a)=>{const i=(0,M.yb)(t),s=u().select(e).select(".nv-wrap").append("g").attr("class",`nv-interval-annotation-layer-${a}`),n=i.color||z((0,T.gO)(i.name),d),l=(0,T.Gr)(i),c=(o[i.name].records||[]).map((e=>{const t=new Date(p().utc(e[i.timeColumn])),a=new Date(p().utc(e[i.intervalEndColumn]));return{...e,[i.timeColumn]:t,[i.intervalEndColumn]:a}})).filter((e=>!Number.isNaN(e[i.timeColumn].getMilliseconds())&&!Number.isNaN(e[i.intervalEndColumn].getMilliseconds())));c.length>0&&s.selectAll("rect").data(c).enter().append("rect").attr({x:e=>Math.min(r(new Date(e[i.timeColumn])),r(new Date(e[i.intervalEndColumn]))),y:0,width:e=>Math.max(Math.abs(r(new Date(e[i.intervalEndColumn]))-r(new Date(e[i.timeColumn]))),1),height:m}).attr("class",`${i.opacity} ${i.style}`).style("stroke-width",i.width).style("stroke",n).style("fill",n).style("fill-opacity",.2).on("mouseover",l.show).on("mouseout",l.hide).call(l),Me.focus&&Me.focus.dispatch.on("onBrush.interval-annotation",(()=>{s.selectAll("rect").data(c).attr({x:e=>r(new Date(e[i.timeColumn])),width:e=>{const t=r(new Date(e[i.timeColumn]));return r(new Date(e[i.intervalEndColumn]))-t}})}))}))),n.datum(a).attr("height",we).attr("width",$e).call(Me),Me.dispatch.on("renderEnd.timeseries-annotation",(()=>{u().selectAll(".slice_container .nv-timeseries-annotation-layer.showMarkerstrue .nv-point").style("stroke-opacity",1).style("fill-opacity",1),u().selectAll(".slice_container .nv-timeseries-annotation-layer.hideLinetrue").style("stroke-width",0)}))}}return(0,T.Aw)(Me),Me}))}V.displayName="NVD3",V.propTypes=Z;const U=V;var W=a(11965);const H=(0,i.Z)(U,{componentWillUnmount:function(){const{id:e}=this.props;null!=e?(0,T.o2)(e):(0,T.Vl)(!0)}}),q=({className:e,...t})=>(0,W.tZ)("div",{className:e},(0,W.tZ)(H,t));q.propTypes={className:n().string.isRequired};const J=(0,s.iK)(q)`
  .superset-legacy-chart-nvd3-dist-bar,
  .superset-legacy-chart-nvd3-bar {
    overflow-x: auto !important;
    svg {
      &.nvd3-svg {
        width: auto;
        font-size: ${({theme:e})=>e.typography.sizes.m};
      }
    }
  }
  .superset-legacy-chart-nvd3 {
    nv-x text {
      font-size: ${({theme:e})=>e.typography.sizes.m};
    }
    g.superset path {
      stroke-dasharray: 5, 5;
    }
    .nvtooltip tr.highlight td {
      font-weight: ${({theme:e})=>e.typography.weights.bold};
      font-size: 15px !important;
    }
    text.nv-axislabel {
      font-size: ${({theme:e})=>e.typography.sizes.m} !important;
    }
    g.solid path,
    line.solid {
      stroke-dasharray: unset;
    }
    g.dashed path,
    line.dashed {
      stroke-dasharray: 5, 5;
    }
    g.longDashed path,
    line.dotted {
      stroke-dasharray: 1, 1;
    }

    g.opacityLow path,
    line.opacityLow {
      stroke-opacity: 0.2;
    }

    g.opacityMedium path,
    line.opacityMedium {
      stroke-opacity: 0.5;
    }
    g.opacityHigh path,
    line.opacityHigh {
      stroke-opacity: 0.8;
    }
    g.time-shift-0 path,
    line.time-shift-0 {
      stroke-dasharray: 5, 5;
    }
    g.time-shift-1 path,
    line.time-shift-1 {
      stroke-dasharray: 1, 5;
    }
    g.time-shift-2 path,
    line.time-shift-3 {
      stroke-dasharray: 5, 1;
    }
    g.time-shift-3 path,
    line.time-shift-3 {
      stroke-dasharray: 5, 1;
    }
    g.time-shift-4 path,
    line.time-shift-4 {
      stroke-dasharray: 5, 10;
    }
    g.time-shift-5 path,
    line.time-shift-5 {
      stroke-dasharray: 0.9;
    }
    g.time-shift-6 path,
    line.time-shift-6 {
      stroke-dasharray: 15, 10, 5;
    }
    g.time-shift-7 path,
    line.time-shift-7 {
      stroke-dasharray: 15, 10, 5, 10;
    }
    g.time-shift-8 path,
    line.time-shift-8 {
      stroke-dasharray: 15, 10, 5, 10, 15;
    }
    g.time-shift-9 path,
    line.time-shift-9 {
      stroke-dasharray: 5, 5, 1, 5;
    }
    .nv-noData.body {
      font-size: ${({theme:e})=>e.typography.sizes.m};
      font-weight: ${({theme:e})=>e.typography.weights.normal};
    }
  }
  .superset-legacy-chart-nvd3-tr-highlight {
    border-top: 1px solid;
    border-bottom: 1px solid;
    font-weight: ${({theme:e})=>e.typography.weights.bold};
  }
  .superset-legacy-chart-nvd3-tr-total {
    font-weight: ${({theme:e})=>e.typography.weights.bold};
  }
  .nvtooltip {
    .tooltip-header {
      white-space: nowrap;
      font-weight: ${({theme:e})=>e.typography.weights.bold};
    }
    tbody tr:not(.tooltip-header) td:nth-child(2) {
      word-break: break-word;
    }
  }
  .d3-tip.nv-event-annotation-layer-table,
  .d3-tip.nv-event-annotation-layer-NATIVE {
    width: 200px;
    border-radius: 2px;
    background-color: #484848;
    fill-opacity: 0.6;
    margin: 8px;
    padding: 8px;
    color: #fff;
    &:after {
      content: '\\25BC';
      font-size: ${({theme:e})=>e.typography.sizes.m};
      color: #484848;
      position: absolute;
      bottom: -14px;
      left: 94px;
    }
  }
`},43323:(e,t,a)=>{a.d(t,{Z:()=>o});var i=a(67294),s=a(11965);function o(e,t){class a extends i.Component{constructor(e){super(e),this.container=void 0,this.setContainerRef=this.setContainerRef.bind(this)}componentDidMount(){this.execute()}componentDidUpdate(){this.execute()}componentWillUnmount(){this.container=void 0,null!=t&&t.componentWillUnmount&&t.componentWillUnmount.bind(this)()}setContainerRef(e){this.container=e}execute(){this.container&&e(this.container,this.props)}render(){const{id:e,className:t}=this.props;return(0,s.tZ)("div",{ref:this.setContainerRef,id:e,className:t})}}const o=a;return e.displayName&&(o.displayName=e.displayName),e.propTypes&&(o.propTypes={...o.propTypes,...e.propTypes}),e.defaultProps&&(o.defaultProps=e.defaultProps),a}},37731:(e,t,a)=>{function i(e){return null!=e}a.d(t,{Z:()=>i})}}]);