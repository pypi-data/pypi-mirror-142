"use strict";
(self["webpackChunkqslwidgets"] = self["webpackChunkqslwidgets"] || []).push([["lib_index_js"],{

/***/ "./lib/ImageLabelerComponent.js":
/*!**************************************!*\
  !*** ./lib/ImageLabelerComponent.js ***!
  \**************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
const react_1 = __importDefault(__webpack_require__(/*! react */ "webpack/sharing/consume/default/react"));
const streamlit_component_lib_1 = __webpack_require__(/*! streamlit-component-lib */ "webpack/sharing/consume/default/streamlit-component-lib/streamlit-component-lib");
const react_image_labeler_1 = __importDefault(__webpack_require__(/*! react-image-labeler */ "webpack/sharing/consume/default/react-image-labeler/react-image-labeler"));
const useStreamlitState = (python) => {
    const [state, setState] = react_1.default.useState(python);
    react_1.default.useEffect(() => {
        setState(python);
    }, [python]);
    react_1.default.useEffect(() => streamlit_component_lib_1.Streamlit.setComponentValue(state), []);
    return [
        state,
        (updated) => {
            setState(updated);
            streamlit_component_lib_1.Streamlit.setComponentValue(updated);
        },
    ];
};
const ImageLabelerComponent = ({ args }) => {
    const [state, setState] = useStreamlitState(args);
    const mode = window.matchMedia &&
        window.matchMedia('(prefers-color-scheme: dark)').matches
        ? 'dark'
        : 'light';
    react_1.default.useEffect(() => streamlit_component_lib_1.Streamlit.setFrameHeight());
    return (react_1.default.createElement("div", null,
        react_1.default.createElement(react_image_labeler_1.default, { src: state.src, labels: state.labels, config: state.config, options: { mode, progress: state.progress }, metadata: state.metadata, callbacks: {
                onSave: (labels) => setState(Object.assign(Object.assign({}, state), { labels })),
                onSaveConfig: state.buttons['config']
                    ? (config) => setState(Object.assign(Object.assign({}, state), { config }))
                    : undefined,
                onNext: state.buttons['next']
                    ? () => setState(Object.assign(Object.assign({}, state), { action: 'next' }))
                    : undefined,
                onPrev: state.buttons['prev']
                    ? () => setState(Object.assign(Object.assign({}, state), { action: 'prev' }))
                    : undefined,
                onDelete: state.buttons['delete']
                    ? () => setState(Object.assign(Object.assign({}, state), { action: 'delete' }))
                    : undefined,
                onIgnore: state.buttons['ignore']
                    ? () => setState(Object.assign(Object.assign({}, state), { action: 'ignore' }))
                    : undefined,
                onUnignore: state.buttons['unignore']
                    ? () => setState(Object.assign(Object.assign({}, state), { action: 'unignore' }))
                    : undefined,
            } })));
};
exports["default"] = streamlit_component_lib_1.withStreamlitConnection(ImageLabelerComponent);
//# sourceMappingURL=ImageLabelerComponent.js.map

/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


// Copyright (c) Fausto Morales
// Distributed under the terms of the MIT License.
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __exportStar = (this && this.__exportStar) || function(m, exports) {
    for (var p in m) if (p !== "default" && !Object.prototype.hasOwnProperty.call(exports, p)) __createBinding(exports, m, p);
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
__exportStar(__webpack_require__(/*! ./version */ "./lib/version.js"), exports);
__exportStar(__webpack_require__(/*! ./ImageLabelerWidget */ "./lib/ImageLabelerWidget.js"), exports);
__exportStar(__webpack_require__(/*! ./ImageLabelerComponent */ "./lib/ImageLabelerComponent.js"), exports);
//# sourceMappingURL=index.js.map

/***/ })

}]);
//# sourceMappingURL=lib_index_js.4f5160f97de2d2c23a08.js.map