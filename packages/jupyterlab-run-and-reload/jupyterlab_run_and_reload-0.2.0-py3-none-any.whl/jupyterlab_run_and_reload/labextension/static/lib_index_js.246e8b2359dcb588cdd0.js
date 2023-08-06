"use strict";
(self["webpackChunkjupyterlab_run_and_reload"] = self["webpackChunkjupyterlab_run_and_reload"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/docmanager */ "webpack/sharing/consume/default/@jupyterlab/docmanager");
/* harmony import */ var _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_4__);





var CommandIDs;
(function (CommandIDs) {
    CommandIDs.reloadAll = 'run-and-reload:run-all-cells-and-reload';
})(CommandIDs || (CommandIDs = {}));
// TODO: Change category to run items
const PALETTE_CATEGORY = 'Run and reload extension';
/**
 * Initialization data for the jupyterlab_run_and_reload extension.
 *
 * TODOs:
 * - Add setting: file extensions to reload
 * - Add setting: only reload visible widgets or not
 * - Add toolbar button in notebook panel with run and reload
 * - Also add "Restart kernel, run all cells and reload PDFs"
 */
const plugin = {
    id: 'jupyterlab_run_and_reload:plugin',
    autoStart: true,
    requires: [_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_2__.IDocumentManager],
    optional: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__.ISettingRegistry, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette],
    activate: (app, manager, settingRegistry, palette) => {
        console.log('JupyterLab extension jupyterlab_run_and_reload is activated!');
        if (settingRegistry) {
            settingRegistry
                .load(plugin.id)
                .then(settings => {
                console.log('jupyterlab_run_and_reload settings loaded:', settings.composite);
            })
                .catch(reason => {
                console.error('Failed to load settings for jupyterlab_run_and_reload.', reason);
            });
        }
        const { shell, commands } = app;
        commands.addCommand(CommandIDs.reloadAll, {
            label: 'Run All Cells and Reload PDFs',
            caption: 'Reload all static files after your notebook is finished running all cells.',
            isEnabled: () => shell.currentWidget instanceof _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_4__.NotebookPanel,
            execute: async () => {
                // Get currently selected widget
                const currentWidget = shell.currentWidget;
                // If current widget is a notebook then we can run all cells
                // If not, then this command does not make sense and should not be callable actually
                if (!(currentWidget instanceof _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_4__.NotebookPanel)) {
                    return;
                }
                function widgetShouldReload(widget) {
                    const context = manager.contextForWidget(widget);
                    return context === null || context === void 0 ? void 0 : context.path.endsWith('.pdf');
                }
                // Get all attached widgets in the shell
                const currentWidgets = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.toArray)(shell.widgets());
                // Obtain the list of widgets that might need to be reloaded after the notebook is finished
                const widgetsToReload = currentWidgets.filter(widgetShouldReload);
                const contextsToReload = widgetsToReload.map(widget => manager.contextForWidget(widget));
                // Connect the openOrReveal function to the fileChanged signal of the relevant widgets
                contextsToReload.forEach(context => {
                    context === null || context === void 0 ? void 0 : context.fileChanged.connect((context, model) => {
                        manager.openOrReveal(context.path);
                    });
                });
                // If current widget is a notebook then we can run all cells
                if (currentWidget instanceof _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_4__.NotebookPanel) {
                    // TODO: Add check on result + notification if notebook run was not successfull
                    await _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_4__.NotebookActions.runAll(currentWidget.content, currentWidget.sessionContext);
                }
                // Loop over all widgets in the shell and revert the relevant ones
                for (const context of contextsToReload) {
                    context === null || context === void 0 ? void 0 : context.revert();
                }
            }
        });
        // Add the command to the palette
        if (palette) {
            palette.addItem({
                command: CommandIDs.reloadAll,
                args: { isPalette: true },
                category: PALETTE_CATEGORY
            });
        }
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.246e8b2359dcb588cdd0.js.map