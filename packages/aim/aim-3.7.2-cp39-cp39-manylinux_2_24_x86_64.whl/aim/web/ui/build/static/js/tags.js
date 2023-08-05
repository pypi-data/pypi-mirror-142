(this.webpackJsonpui_v2=this.webpackJsonpui_v2||[]).push([[17],{1249:function(e,t,a){},1284:function(e,t,a){"use strict";a.r(t);var n,o,i=a(0),c=a.n(i),r=a(7),l=a(204),s=a(228),d=a(3),u=a(205),g=a.n(u),j=a(221),m=a(46),b=a(538),v=a(226),h=Object(v.a)({isTagsDataLoading:!1,isRunsDataLoading:!1,isTagInfoDataLoading:!1,notifyData:[]});function f(e){var t,a=(null===(t=h.getState())||void 0===t?void 0:t.notifyData)||[];a=Object(m.a)(a).filter((function(t){return t.id!==e})),h.setState({notifyData:a})}function _(e){var t,a=(null===(t=h.getState())||void 0===t?void 0:t.notifyData)||[];a=[].concat(Object(m.a)(a),[e]),h.setState({notifyData:a}),setTimeout((function(){f(e.id)}),3e3)}var O=Object(d.a)(Object(d.a)({},h),{},{initialize:function(){h.init()},getTagsData:function(){var e=b.a.getTags(),t=e.call;return{call:function(){h.setState({isTagsDataLoading:!0}),t().then((function(e){h.setState({tagsList:e,isTagsDataLoading:!1})}))},abort:e.abort}},getTagRuns:function(e){var t,a;return n&&(null===(a=n)||void 0===a||a.abort()),n=b.a.getTagRuns(e),{call:function(){var e=Object(j.a)(g.a.mark((function e(){var t;return g.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return h.setState({isRunsDataLoading:!0}),e.next=3,n.call();case 3:t=e.sent,h.setState({tagRuns:t.runs,isRunsDataLoading:!1});case 5:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}(),abort:null===(t=n)||void 0===t?void 0:t.abort}},archiveTag:function(e){var t=arguments.length>1&&void 0!==arguments[1]&&arguments[1],a=h.getState();return b.a.hideTag(e,t).call().then((function(){h.setState(Object(d.a)(Object(d.a)({},a),{},{tagInfo:Object(d.a)(Object(d.a)({},null===a||void 0===a?void 0:a.tagInfo),{},{archived:t})})),_({id:Date.now(),severity:"success",messages:[t?"Tag successfully archived":"Tag successfully unarchived"]})}))},getTagById:function(e){var t,a;return o&&(null===(a=o)||void 0===a||a.abort()),o=b.a.getTagById(e),{call:function(){var e=Object(j.a)(g.a.mark((function e(){var t;return g.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return h.setState({isTagInfoDataLoading:!0}),e.next=3,o.call();case 3:t=e.sent,h.setState({tagInfo:t,isTagInfoDataLoading:!1});case 5:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}(),abort:null===(t=o)||void 0===t?void 0:t.abort}},updateTagInfo:function(e){var t=h.getState();h.setState(Object(d.a)(Object(d.a)({},t),{},{tagInfo:e}))},onNotificationDelete:f,deleteTag:function(e){return b.a.deleteTag(e).call().then((function(){_({id:Date.now(),severity:"success",messages:["Tag successfully deleted"]})}))},createTag:function(e){return b.a.createTag(e).call().then((function(e){return e.id?_({id:Date.now(),severity:"success",messages:["Tag successfully created"]}):_({id:Date.now(),severity:"error",messages:[e.detail]}),e}))},updateTag:function(e,t){return b.a.updateTag(e,t).call().then((function(e){return e.id?_({id:Date.now(),severity:"success",messages:["Tag successfully updated"]}):_({id:Date.now(),severity:"error",messages:[e.detail]}),e}))}}),T=a(203),x=a(16),p=a(248),C=a(1289),D=a(1279),y=a(1301),N=a(1);function L(e){var t=e.children,a=e.value,n=e.index,o=e.className;return Object(N.jsx)(r.a,{children:Object(N.jsx)("div",{role:"tabpanel",hidden:a!==n,id:"wrapped-tabpanel-".concat(n),"aria-labelledby":"wrapped-tab-".concat(n),className:o,children:a===n&&Object(N.jsx)(y.a,{children:t})})})}var w=Object(i.memo)(L),I=a(509),S=a(438),R=a(428),F=a(430),B=a(445),M=a(1086),k=a(132),A=a(273),G=a(1088),z=a(1280),E=a(4),H=a(207),P=(a(1249),Object(z.a)({tagColor:{border:function(e){var t=e.colorName,a=e.color;return"1px solid ".concat(t===a?a:"transparent")},"&:hover, &:focus":{border:function(e){var t=e.colorName;return"1px solid ".concat(t," !important;")},backgroundColor:"inherit"}}}));function U(e){var t=e.colorName,a=e.onColorButtonClick,n=e.color,o=P({color:n,colorName:t}).tagColor;return Object(N.jsx)(R.a,{className:"TagForm__tagFormContainer__colorContainer__colorBox__colorButton ".concat(o),onClick:function(){return a(t)},children:Object(N.jsxs)(N.Fragment,{children:[Object(N.jsx)("span",{className:"TagForm__tagFormContainer__colorContainer__colorBox__colorButton__content",style:{background:t}}),Object(N.jsx)("span",{className:"TagForm__tagFormContainer__colorContainer__colorBox__colorButton__circle",style:{background:t}})]})})}function V(e){var t=e.tagData,a=e.editMode,n=e.tagId,o=e.onCloseModal,c=Object(G.a)({initialValues:a?{name:(null===t||void 0===t?void 0:t.name)||"",color:(null===t||void 0===t?void 0:t.color)||H.b[0][0],comment:(null===t||void 0===t?void 0:t.description)||""}:{name:"",color:H.b[0][0],comment:""},onSubmit:k.a,validationSchema:M.a({name:M.b().required("Required field").max(50,"Must be 50 characters or fewer"),comment:M.b().max(100,"Must be 100 characters or fewer")})}),s=c.values,d=c.errors,u=c.touched,g=c.setFieldValue,j=c.setValues,m=c.setFieldTouched,b=c.submitForm,v=c.validateForm,h=s.name,f=s.color,_=s.comment;function x(e,t){var a;g(t,null===e||void 0===e||null===(a=e.target)||void 0===a?void 0:a.value,!0).then((function(){m(t,!0)}))}var p=Object(i.useMemo)((function(){return H.b[0].map((function(e,t){return Object(N.jsx)(U,{color:f,colorName:e,onColorButtonClick:C},e)}))}),[f]);function C(e){g("color",e)}return Object(N.jsx)(r.a,{children:Object(N.jsxs)("div",{className:"TagForm",children:[Object(N.jsxs)("div",{className:"TagForm__tagFormContainer",children:[Object(N.jsx)(E.m,{component:"p",tint:60,children:"Name"}),Object(N.jsx)(S.a,{placeholder:"Name",variant:"outlined",className:"TagForm__tagFormContainer__TextField TextField__OutLined__Medium",onChange:function(e){return x(e,"name")},value:h,size:"small",error:!(!u.name||!d.name),helperText:u.name&&d.name}),Object(N.jsx)(E.m,{component:"p",tint:60,children:"Comment"}),Object(N.jsx)(S.a,{placeholder:"Comment",variant:"outlined",onChange:function(e){return x(e,"comment")},className:"TagForm__tagFormContainer__TextField TextField__TextArea__OutLined__Small",multiline:!0,value:_,error:!(!u.comment||!d.comment),helperText:u.comment&&d.comment}),Object(N.jsxs)("div",{className:"TagForm__tagFormContainer__colorContainer",children:[Object(N.jsx)(E.m,{component:"p",tint:50,children:"Colors"}),Object(N.jsx)("div",{className:"TagForm__tagFormContainer__colorContainer__colorBox",children:p})]}),Object(N.jsxs)("div",{className:"TagForm__tagFormContainer__previewContainer",children:[Object(N.jsx)(E.m,{component:"p",tint:30,children:"Preview"}),Object(N.jsx)("div",{className:"TagForm__tagFormContainer__previewContainer__tagPreviewBox",children:Object(N.jsx)(E.c,{label:h||"Tag Preview",color:f})})]})]}),Object(N.jsxs)("div",{className:"TagForm__tagFormFooterContainer",children:[Object(N.jsx)(R.a,{onClick:a?function(){j({name:(null===t||void 0===t?void 0:t.name)||"",color:(null===t||void 0===t?void 0:t.color)||"",comment:(null===t||void 0===t?void 0:t.description)||""},!0)}:o,className:"TagForm__tagFormFooterContainer__cancelButton",color:"secondary",children:a?"Reset":"Cancel"}),Object(N.jsx)(R.a,{onClick:a?function(){b().then((function(){return v(s).then((function(e){Object(A.a)(e)&&O.updateTag({name:h,color:f,description:_},n||"").then((function(){O.getTagsData().call(),O.getTagById(n||"").call(),o()}))}))}))}:function(){Object(T.b)(l.a.tags.create),b().then((function(){return v(s).then((function(e){Object(A.a)(e)&&O.createTag({name:h,color:f,description:_}).then((function(e){e.id&&(o(),O.getTagsData().call())}))}))}))},variant:"contained",color:"primary",children:a?"Save":"Create"})]})]})})}var K=Object(i.memo)(V),q=a(437),J=a(231),Y=a(116);function W(e){var t=e.tableRef,a=e.tagsList,n=e.hasSearchValue,o=e.isTagsDataLoading,c=e.onTableRunClick,l=e.onSoftDeleteModalToggle,s=e.onUpdateModalToggle,d=e.onDeleteModalToggle,u=Object(i.useState)(""),g=Object(x.a)(u,2),j=g[0],m=g[1],b=[{dataKey:"name",key:"name",title:"Name & Color",width:200,cellRenderer:function(e,t){var a=e.cellData,n=a.name,o=a.color;return Object(N.jsx)(E.c,{label:n,color:o,maxWidth:"100%"},t)}},{dataKey:"runs",key:"runs",title:"Runs",width:150,cellRenderer:function(e,t){var a=e.cellData;return Object(N.jsxs)("div",{className:"TagsTable__runsCell",children:[Object(N.jsx)("span",{className:"TagsTable__runsCell--iconBox",children:Object(N.jsx)(E.g,{name:"circle-with-dot"})}),Object(N.jsx)(E.m,{size:14,color:"info",children:a.count})]})}},{dataKey:"comment",key:"comment",title:"Comment",width:0,flexGrow:1,cellRenderer:function(e){var t=e.cellData;e.i;return Object(N.jsxs)("div",{className:"TagsTable__commentCell",role:"button","aria-pressed":"false",onClick:function(e){return e.stopPropagation()},children:[Object(N.jsx)(E.m,{size:14,tint:100,children:t.description}),t.id===j&&Object(N.jsxs)("div",{className:"TagsTable__commentCell__actionsContainer",children:[!(null===t||void 0===t?void 0:t.archived)&&Object(N.jsx)(E.d,{withOnlyIcon:!0,onClick:function(){return e=t,O.updateTagInfo(e),void s();var e},children:Object(N.jsx)(E.g,{color:"primary",name:"edit"})}),(null===t||void 0===t?void 0:t.archived)?Object(N.jsx)(E.d,{withOnlyIcon:!0,onClick:function(){return v(t)},children:Object(N.jsx)(E.g,{color:"primary",name:"eye-show-outline"})}):Object(N.jsx)(E.d,{withOnlyIcon:!0,onClick:function(){return v(t)},children:Object(N.jsx)(E.g,{color:"primary",name:"eye-outline-hide"})}),Object(N.jsx)(E.d,{onClick:function(){return e=t,O.updateTagInfo(e),void d();var e},withOnlyIcon:!0,children:Object(N.jsx)(E.g,{fontSize:"small",name:"delete",color:"primary"})})]})]})}}];function v(e){O.updateTagInfo(e),l()}return Object(i.useEffect)((function(){var e;t.current.updateData&&(null===t||void 0===t||null===(e=t.current)||void 0===e||e.updateData({newData:a.map((function(e,t){return{key:e.id,name:{name:e.name,color:e.color},comment:e,runs:{count:e.run_count,tagId:e.id}}})),newColumns:b}))}),[a,c,j]),Object(N.jsx)(r.a,{children:Object(N.jsxs)("div",{className:"Tags__TagList__tagListBox",children:[!o&&!q.a.isNil(a)&&Object(N.jsx)("div",{className:"Tags__TagList__tagListBox__titleBox",children:Object(N.jsxs)(E.m,{component:"h4",size:14,weight:600,tint:100,children:[a.length," ",a.length>1?"Tags":"Tag"]})}),Object(N.jsx)(J.a,{ref:t,fixed:!1,columns:b,data:null,isLoading:o,hideHeaderActions:!0,rowHeight:52,headerHeight:32,onRowHover:function(e){return m(e)},onRowClick:function(e){return c(e||"")},illustrationConfig:{type:n?Y.c.EmptySearch:Y.c.ExploreData,page:"tags"},height:"100%"})]})})}var Q=Object(i.memo)(W),X=a(123),Z=a(225),$=a(153),ee=a(160),te=a.n(ee);function ae(e){var t=e.runsList,a=Object(i.useRef)({}),n=[{dataKey:"runs",key:"runs",title:"Runs",width:400,cellRenderer:function(e){var t=e.cellData;return Object(N.jsx)($.c,{to:"/runs/".concat(t.id),children:Object(N.jsx)("p",{className:"TagsTable__runName",children:t.name})})}},{dataKey:"createdDate",key:"createdDate",title:"Created at",width:400,cellRenderer:function(e){var t=e.cellData;return Object(N.jsx)("p",{className:"TagsTable__runCreatedDate",children:t})}}];return Object(i.useEffect)((function(){var e;t&&(null===a||void 0===a||null===(e=a.current)||void 0===e||e.updateData({newData:t.map((function(e){return{runs:{name:e.run_id,id:e.run_id},createdDate:te()(e.creation_time).format("DD-MM-YY HH:mm")}})),newColumns:n}))}),[t]),Object(N.jsx)(r.a,{children:Object(N.jsx)("div",{className:"TagsTable",children:Object(N.jsx)(J.a,{ref:a,fixed:!1,columns:n,data:[],hideHeaderActions:!0,rowHeight:32,headerHeight:32})})})}var ne=Object(i.memo)(ae);a(951);function oe(e){var t=e.id,a=e.onSoftDeleteModalToggle,n=e.onUpdateModalToggle,o=e.onDeleteModalToggle,c=e.isTagInfoDataLoading,l=e.tagInfo,s=e.isRunsDataLoading,d=e.tagRuns;return Object(i.useEffect)((function(){var e=O.getTagById(t),a=O.getTagRuns(t);return a.call(),e.call(),function(){a.abort(),e.abort()}}),[t]),Object(N.jsx)(r.a,{children:Object(N.jsxs)("div",{className:"TagDetail",children:[Object(N.jsxs)("div",{className:"TagDetail__headerContainer",children:[Object(N.jsx)(X.a,{isLoading:c,loaderType:"skeleton",loaderConfig:{variant:"rect",width:100,height:24},width:"auto",children:l&&Object(N.jsx)(E.c,{size:"medium",color:null===l||void 0===l?void 0:l.color,label:null===l||void 0===l?void 0:l.name})}),Object(N.jsxs)("div",{className:"TagDetail__headerContainer__headerActionsBox",children:[!(null===l||void 0===l?void 0:l.archived)&&Object(N.jsx)(E.d,{withOnlyIcon:!0,onClick:n,children:Object(N.jsx)(E.g,{name:"edit"})}),(null===l||void 0===l?void 0:l.archived)?Object(N.jsx)(E.d,{onClick:a,withOnlyIcon:!0,children:Object(N.jsx)(E.g,{name:"eye-show-outline",color:"primary"})}):Object(N.jsx)(E.d,{withOnlyIcon:!0,onClick:a,children:Object(N.jsx)(E.g,{name:"eye-outline-hide",color:"primary"})}),Object(N.jsx)(E.d,{withOnlyIcon:!0,onClick:o,children:Object(N.jsx)(E.g,{name:"delete",fontSize:"small",color:"primary"})})]})]}),Object(N.jsx)(X.a,{isLoading:s,className:"Tags__TagList__tagListBusyLoader",children:Object(A.a)(d)?Object(N.jsx)(Z.a,{size:"xLarge",title:"No Runs"}):Object(N.jsx)(ne,{runsList:d})})]})})}var ie=Object(i.memo)(oe),ce=a(928);function re(e){var t,a,n,o,c=e.tagInfo,l=e.tagHash,s=e.onSoftDeleteModalToggle,d=e.onTagDetailOverlayToggle,u=e.isTagDetailOverLayOpened,g=e.modalIsOpen,j=Object(i.useRef)({archived:null===c||void 0===c?void 0:c.archived});return Object(N.jsx)(r.a,{children:Object(N.jsx)(ce.a,{open:g,onCancel:s,onSubmit:(null===(t=j.current)||void 0===t||t.archived,function(){O.archiveTag(l,!(null===c||void 0===c?void 0:c.archived)).then((function(){O.getTagsData().call(),s(),u&&d()}))}),text:"Are you sure you want to ".concat((null===(a=j.current)||void 0===a?void 0:a.archived)?"bring back":"hide"," this tag?"),icon:(null===(n=j.current)||void 0===n?void 0:n.archived)?Object(N.jsx)(E.g,{name:"eye-show-outline"}):Object(N.jsx)(E.g,{name:"eye-outline-hide"}),title:"Are you sure?",confirmBtnText:(null===(o=j.current)||void 0===o?void 0:o.archived)?"Bring back":"Hide"})})}var le=Object(i.memo)(re);function se(e){var t=e.tagInfo,a=e.tagHash,n=e.onDeleteModalToggle,o=e.onTagDetailOverlayToggle,i=e.isTagDetailOverLayOpened,c=e.modalIsOpen,l=Object(G.a)({initialValues:{name:""},onSubmit:k.a,validationSchema:M.a({name:M.b().test("name","Name does not match",(function(e){return e===t.name}))})}),s=l.values,d=l.errors,u=l.touched,g=l.setFieldValue,j=l.setFieldTouched,m=l.submitForm,b=l.validateForm,v=s.name;function h(){g("name",""),j("name",!1),n()}return Object(N.jsx)(r.a,{children:Object(N.jsxs)(ce.a,{open:c,onCancel:h,onSubmit:function(){m().then((function(){return b(s).then((function(e){Object(A.a)(e)&&O.deleteTag(a).then((function(){O.getTagsData().call(),i&&o(),h()}))}))}))},text:"Are you sure you want to delete this tag?",icon:Object(N.jsx)(E.g,{name:"delete"}),title:"Are you sure?",statusType:"error",confirmBtnText:"Delete",children:[Object(N.jsx)(E.m,{component:"p",weight:400,tint:100,className:"TagDelete__contentContainer__contentBox__warningText",children:'Please type "'.concat(null===t||void 0===t?void 0:t.name,'" to confirm:')}),Object(N.jsx)(S.a,{label:"Name",value:v,id:"name",variant:"outlined",className:"TagForm__tagFormContainer__labelField TextField__OutLined__Small",size:"small",onChange:function(e){var t;g("name",null===e||void 0===e||null===(t=e.target)||void 0===t?void 0:t.value,!0).then((function(){j("name",!0)}))},error:!(!u.name||!d.name),helperText:u.name&&d.name})]})})}var de=Object(i.memo)(se);function ue(e){var t=e.tagsList,a=e.isHiddenTagsList,n=e.isTagsDataLoading,o=e.tagInfo,c=e.tagRuns,s=e.isRunsDataLoading,d=e.isTagInfoDataLoading,u=Object(i.useRef)({}),g=Object(i.useState)(!1),j=Object(x.a)(g,2),m=j[0],b=j[1],v=Object(i.useState)(!1),h=Object(x.a)(v,2),f=h[0],_=h[1],O=Object(i.useState)(!1),p=Object(x.a)(O,2),C=p[0],D=p[1],y=Object(i.useState)(!1),L=Object(x.a)(y,2),w=L[0],I=L[1],M=Object(i.useState)(!1),k=Object(x.a)(M,2),A=k[0],G=k[1],z=Object(i.useState)(""),H=Object(x.a)(z,2),P=H[0],U=H[1],V=Object(i.useState)(""),q=Object(x.a)(V,2),J=q[0],Y=q[1];function W(){b(!m)}function X(){_(!f)}function Z(){D(!C)}function $(){I(!w)}function ee(){var e;A&&(null===(e=u.current)||void 0===e||e.setActiveRow(null));G(!A)}return Object(N.jsxs)("div",{className:"Tags__TagList",children:[Object(N.jsxs)("div",{className:"Tags__TagList__header",children:[Object(N.jsx)(S.a,{placeholder:"Search",variant:"outlined",InputProps:{startAdornment:Object(N.jsx)(E.g,{name:"search"}),disabled:n},onChange:function(e){Y(e.target.value)},value:J}),!a&&Object(N.jsxs)(R.a,{variant:"contained",size:"small",className:"Tags__TagList__header__createButton",color:"primary",onClick:W,children:[Object(N.jsx)(E.g,{name:"plus"}),"Create Tag"]})]}),Object(N.jsxs)(r.a,{children:[Object(N.jsx)(Q,{tableRef:u,tagsList:t.filter((function(e){return e.name.includes(J)})),isTagsDataLoading:n,hasSearchValue:!!J,onTableRunClick:function(e){A||G(!0),U(e),T.b(l.a.tags.tagDetail)},onSoftDeleteModalToggle:Z,onDeleteModalToggle:$,onUpdateModalToggle:X}),Object(N.jsx)(F.a,{onClose:W,"aria-labelledby":"customized-dialog-title",open:m,children:Object(N.jsxs)("div",{className:"Tags__TagList__modalContainer",children:[Object(N.jsx)("div",{className:"Tags__TagList__modalContainer__titleBox",children:Object(N.jsx)(E.m,{component:"h4",weight:600,tint:100,size:14,children:"Create Tag"})}),Object(N.jsx)("div",{className:"Tags__TagList__modalContainer__contentBox",children:Object(N.jsx)(K,{onCloseModal:W})})]})},(null===o||void 0===o?void 0:o.id)+"1"),Object(N.jsx)(F.a,{onClose:X,"aria-labelledby":"customized-dialog-title",open:f,children:Object(N.jsxs)("div",{className:"Tags__TagList__modalContainer",children:[Object(N.jsx)("div",{className:"Tags__TagList__modalContainer__titleBox",children:Object(N.jsx)(E.m,{component:"h4",size:14,tint:100,weight:600,children:"Update Tag"})}),Object(N.jsx)("div",{className:"Tags__TagList__modalContainer__contentBox",children:Object(N.jsx)(K,{onCloseModal:X,tagData:o,tagId:null===o||void 0===o?void 0:o.id,editMode:!0})})]})},(null===o||void 0===o?void 0:o.id)+"2"),o&&Object(N.jsx)(le,{modalIsOpen:C,tagInfo:o,tagHash:null===o||void 0===o?void 0:o.id,onSoftDeleteModalToggle:Z,onTagDetailOverlayToggle:ee,isTagDetailOverLayOpened:A}),o&&Object(N.jsx)(de,{modalIsOpen:w,tagInfo:o,tagHash:null===o||void 0===o?void 0:o.id,onDeleteModalToggle:$,onTagDetailOverlayToggle:ee,isTagDetailOverLayOpened:A},null===o||void 0===o?void 0:o.id)]}),Object(N.jsx)(B.a,{className:"Tags__TagList__overLayContainer",anchor:"right",open:A,onClose:ee,children:A&&Object(N.jsx)(ie,{id:P,onSoftDeleteModalToggle:Z,onUpdateModalToggle:X,onDeleteModalToggle:$,tagRuns:c,tagInfo:o,isRunsDataLoading:s,isTagInfoDataLoading:d})})]})}var ge=Object(i.memo)(ue);function je(e){var t=e.tagsListData,a=e.isTagsDataLoading,n=e.tagInfo,o=e.tagRuns,c=e.onNotificationDelete,s=e.notifyData,d=e.isRunsDataLoading,u=e.isTagInfoDataLoading,g=Object(i.useState)(0),j=Object(x.a)(g,2),m=j[0],b=j[1],v=Object(i.useState)((null===t||void 0===t?void 0:t.filter((function(e){return e.archived})))||[]),h=Object(x.a)(v,2),f=h[0],_=h[1],O=Object(i.useState)((null===t||void 0===t?void 0:t.filter((function(e){return!e.archived})))||[]),y=Object(x.a)(O,2),L=y[0],S=y[1];return Object(i.useEffect)((function(){_((null===t||void 0===t?void 0:t.filter((function(e){return e.archived})))||[]),S((null===t||void 0===t?void 0:t.filter((function(e){return!e.archived})))||[])}),[t]),Object(N.jsx)(r.a,{children:Object(N.jsxs)("section",{className:"Tags container",children:[Object(N.jsx)(p.a,{className:"Tags__tabsContainer",children:Object(N.jsxs)(C.a,{value:m,onChange:function(e,t){b(t),T.b(l.a.tags.tabChange)},"aria-label":"simple tabs example",indicatorColor:"primary",className:"Tags__tabsContainer__tabs",children:[Object(N.jsx)(D.a,{label:"Tags"}),Object(N.jsx)(D.a,{label:"Hidden Tags"})]})}),Object(N.jsx)(r.a,{children:Object(N.jsx)(w,{value:m,index:0,className:"Tags__tabPanel",children:Object(N.jsx)(ge,{tagsList:L,isTagsDataLoading:a,tagInfo:n,tagRuns:o,isRunsDataLoading:d,isTagInfoDataLoading:u})})}),Object(N.jsx)(r.a,{children:Object(N.jsx)(w,{value:m,index:1,className:"Tags__tabPanel",children:Object(N.jsx)(ge,{tagsList:f,isHiddenTagsList:!0,isTagsDataLoading:a,tagInfo:n,tagRuns:o,isRunsDataLoading:d,isTagInfoDataLoading:u})})}),(null===s||void 0===s?void 0:s.length)>0&&Object(N.jsx)(I.a,{handleClose:c,data:s})]})})}var me=Object(i.memo)(je),be=O.getTagsData();t.default=function(){var e=Object(s.a)(O);return c.a.useEffect((function(){O.initialize(),be.call(),T.a(l.a.tags.pageView)}),[]),Object(N.jsx)(r.a,{children:Object(N.jsx)(me,{tagsListData:null===e||void 0===e?void 0:e.tagsList,isTagsDataLoading:null===e||void 0===e?void 0:e.isTagsDataLoading,tagInfo:null===e||void 0===e?void 0:e.tagInfo,tagRuns:null===e||void 0===e?void 0:e.tagRuns,onNotificationDelete:O.onNotificationDelete,notifyData:null===e||void 0===e?void 0:e.notifyData,isRunsDataLoading:null===e||void 0===e?void 0:e.isRunsDataLoading,isTagInfoDataLoading:null===e||void 0===e?void 0:e.isTagInfoDataLoading})})}},505:function(e,t,a){},509:function(e,t,a){"use strict";a.d(t,"a",(function(){return d}));a(0);var n=a(1295),o=a(1298),i=a(1301),c=a.p+"static/media/successIcon.bd3fad23.svg",r=a.p+"static/media/errorIcon.09cae82c.svg",l=a(7),s=(a(505),a(1));function d(e){var t=e.data,a=e.handleClose;return Object(s.jsx)(l.a,{children:Object(s.jsx)("div",{children:Object(s.jsx)(o.a,{open:!0,autoHideDuration:3e3,anchorOrigin:{vertical:"top",horizontal:"right"},children:Object(s.jsx)("div",{className:"NotificationContainer",children:t.map((function(e){var t=e.id,o=e.severity,l=e.messages;return Object(s.jsx)(i.a,{mt:.5,children:Object(s.jsx)(n.a,{onClose:function(){return a(+t)},variant:"outlined",severity:o,iconMapping:{success:Object(s.jsx)("img",{src:c,alt:""}),error:Object(s.jsx)("img",{src:r,alt:""})},style:{height:"auto"},children:Object(s.jsxs)("div",{className:"NotificationContainer__contentBox",children:[Object(s.jsx)("p",{className:"NotificationContainer__contentBox__severity",children:o}),l.map((function(e,t){return Object(s.jsx)("p",{className:"NotificationContainer__contentBox__message",children:e},t)}))]})})},t)}))})})})})}},538:function(e,t,a){"use strict";var n=a(162),o={GET_TAGS:"tags",GET_TAG:"tags/",CREATE_TAG:"tags",UPDATE_TAG:"tags/",GET_TAG_RUNS:function(e){return"tags/".concat(e,"/runs")}};var i={endpoints:o,getTags:function(){return n.a.get(o.GET_TAGS)},createTag:function(e){return n.a.post(o.GET_TAGS,e,{headers:{"Content-Type":"application/json"}})},updateTag:function(e,t){return n.a.put(o.UPDATE_TAG+t,e,{headers:{"Content-Type":"application/json"}})},getTagById:function(e){return n.a.get(o.GET_TAG+e)},getTagRuns:function(e){return n.a.get(o.GET_TAG_RUNS(e))},hideTag:function(e,t){return n.a.put(o.GET_TAG+e,{archived:t},{headers:{"Content-Type":"application/json"}})},deleteTag:function(e){return n.a.delete(o.GET_TAG+e,{headers:{"Content-Type":"application/json"}})}};t.a=i},928:function(e,t,a){"use strict";var n=a(0),o=a.n(n),i=a(430),c=a(4),r=a(7),l=(a(946),a(1));function s(e){return Object(l.jsx)(r.a,{children:Object(l.jsxs)(i.a,{open:e.open,onClose:e.onCancel,"aria-labelledby":"dialog-title","aria-describedby":"dialog-description",PaperProps:{elevation:10},className:"ConfirmModal ConfirmModal__".concat(e.statusType),children:[Object(l.jsxs)("div",{className:"ConfirmModal__Body",children:[Object(l.jsx)(c.d,{size:"small",className:"ConfirmModal__Close__Icon",color:"secondary",withOnlyIcon:!0,onClick:e.onCancel,children:Object(l.jsx)(c.g,{name:"close"})}),Object(l.jsxs)("div",{className:"ConfirmModal__Title__Container",children:[Object(l.jsx)("div",{className:"ConfirmModal__Icon",children:e.icon}),e.title&&Object(l.jsx)(c.m,{size:16,tint:100,component:"h4",weight:600,children:e.title})]}),Object(l.jsxs)("div",{children:[e.text&&Object(l.jsx)(c.m,{size:14,className:"ConfirmModal__description",weight:400,component:"p",id:"dialog-description",children:e.title}),Object(l.jsxs)("div",{children:[e.text&&Object(l.jsx)(c.m,{className:"ConfirmModal__description",weight:400,component:"p",id:"dialog-description",children:e.text||""}),e.children&&e.children]})]})]}),Object(l.jsxs)("div",{className:"ConfirmModal__Footer",children:[Object(l.jsx)(c.d,{onClick:e.onCancel,className:"ConfirmModal__CancelButton",children:e.cancelBtnText}),Object(l.jsx)(c.d,{onClick:e.onSubmit,color:"primary",variant:"contained",className:"ConfirmModal__ConfirmButton",autoFocus:!0,children:e.confirmBtnText})]})]})})}s.defaultProps={confirmBtnText:"Confirm",cancelBtnText:"Cancel",statusType:"info"},s.displayName="ConfirmModal",t.a=o.a.memo(s)},946:function(e,t,a){},951:function(e,t,a){}}]);
//# sourceMappingURL=tags.js.map?version=16f5c1866bb142dc56c3