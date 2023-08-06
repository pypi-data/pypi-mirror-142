/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./packages/superset-ui-switchboard/src/switchboard.ts":
/*!*************************************************************!*\
  !*** ./packages/superset-ui-switchboard/src/switchboard.ts ***!
  \*************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

eval("/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"Switchboard\": () => (/* binding */ Switchboard)\n/* harmony export */ });\n/* module decorator */ module = __webpack_require__.hmd(module);\n(function () {var enterModule = typeof reactHotLoaderGlobal !== 'undefined' ? reactHotLoaderGlobal.enterModule : undefined;enterModule && enterModule(module);})();var __signature__ = typeof reactHotLoaderGlobal !== 'undefined' ? reactHotLoaderGlobal.default.signature : function (a) {return a;}; /*\n * Licensed to the Apache Software Foundation (ASF) under one\n * or more contributor license agreements.  See the NOTICE file\n * distributed with this work for additional information\n * regarding copyright ownership.  The ASF licenses this file\n * to you under the Apache License, Version 2.0 (the\n * \"License\"); you may not use this file except in compliance\n * with the License.  You may obtain a copy of the License at\n *\n *   http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing,\n * software distributed under the License is distributed on an\n * \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY\n * KIND, either express or implied.  See the License for the\n * specific language governing permissions and limitations\n * under the License.\n */\n/**\n * A utility for communications between an iframe and its parent, used by the Superset embedded SDK.\n * This builds useful patterns on top of the basic functionality offered by MessageChannel.\n *\n * Both windows instantiate a Switchboard, passing in their MessagePorts.\n * Calling methods on the switchboard causes messages to be sent through the channel.\n */\nclass Switchboard {\n\n\n\n  // used to make unique ids\n\n\n  constructor({ port, name = 'switchboard', debug = false }) {this.port = void 0;this.name = void 0;this.methods = {};this.incrementor = 1;this.debugMode = void 0;\n    this.port = port;\n    this.name = name;\n    this.debugMode = debug;\n    port.addEventListener('message', async (event) => {\n      this.log('message received', event);\n      const message = event.data;\n      if (isGet(message)) {\n        // find the method, call it, and reply with the result\n        this.port.postMessage(await this.getMethodResult(message));\n      } else\n      if (isEmit(message)) {\n        const { method, args } = message;\n        // Find the method and call it, but no result necessary.\n        // Should this multicast to a set of listeners?\n        // Maybe, but that requires writing a bunch more code\n        // and I haven't found a need for it yet.\n        const executor = this.methods[method];\n        if (executor) {\n          executor(args);\n        }\n      }\n    });\n  }\n  async getMethodResult({ messageId, method, args }) {\n    const executor = this.methods[method];\n    if (executor == null) {\n      return {\n        switchboardAction: Actions.ERROR,\n        messageId,\n        error: `[${this.name}] Method \"${method}\" is not defined` };\n\n    }\n    try {\n      const result = await executor(args);\n      return {\n        switchboardAction: Actions.REPLY,\n        messageId,\n        result };\n\n    }\n    catch (err) {\n      this.logError(err);\n      return {\n        switchboardAction: Actions.ERROR,\n        messageId,\n        error: `[${this.name}] Method \"${method}\" threw an error` };\n\n    }\n  }\n  /**\n   * Defines a method that can be \"called\" from the other side by sending an event.\n   */\n  defineMethod(methodName, executor) {\n    this.methods[methodName] = executor;\n  }\n  /**\n   * Calls a method registered on the other side, and returns the result.\n   *\n   * How this is accomplished:\n   * This switchboard sends a \"get\" message over the channel describing which method to call with which arguments.\n   * The other side's switchboard finds a method with that name, and calls it with the arguments.\n   * It then packages up the returned value into a \"reply\" message, sending it back to us across the channel.\n   * This switchboard has attached a listener on the channel, which will resolve with the result when a reply is detected.\n   *\n   * Instead of an arguments list, arguments are supplied as a map.\n   *\n   * @param method the name of the method to call\n   * @param args arguments that will be supplied. Must be serializable, no functions or other nonense.\n   * @returns whatever is returned from the method\n   */\n  get(method, args = undefined) {\n    return new Promise((resolve, reject) => {\n      // In order to \"call a method\" on the other side of the port,\n      // we will send a message with a unique id\n      const messageId = this.getNewMessageId();\n      // attach a new listener to our port, and remove it when we get a response\n      const listener = (event) => {\n        const message = event.data;\n        if (message.messageId !== messageId)\n        return;\n        this.port.removeEventListener('message', listener);\n        if (isReply(message)) {\n          resolve(message.result);\n        } else\n        {\n          const errStr = isError(message) ?\n          message.error :\n          'Unexpected response message';\n          reject(new Error(errStr));\n        }\n      };\n      this.port.addEventListener('message', listener);\n      this.port.start();\n      const message = {\n        switchboardAction: Actions.GET,\n        method,\n        messageId,\n        args };\n\n      this.port.postMessage(message);\n    });\n  }\n  /**\n   * Emit calls a method on the other side just like get does.\n   * But emit doesn't wait for a response, it just sends and forgets.\n   *\n   * @param method\n   * @param args\n   */\n  emit(method, args = undefined) {\n    const message = {\n      switchboardAction: Actions.EMIT,\n      method,\n      args };\n\n    this.port.postMessage(message);\n  }\n  start() {\n    this.port.start();\n  }\n  log(...args) {\n    if (this.debugMode) {\n      console.debug(`[${this.name}]`, ...args);\n    }\n  }\n  logError(...args) {\n    console.error(`[${this.name}]`, ...args);\n  }\n  getNewMessageId() {\n    // eslint-disable-next-line no-plusplus\n    return `m_${this.name}_${this.incrementor++}`;\n  } // @ts-ignore\n  __reactstandin__regenerateByEval(key, code) {// @ts-ignore\n    this[key] = eval(code);}} // Each message we send on the channel specifies an action we want the other side to cooperate with.\nvar Actions;\n(function (Actions) {\n  Actions[\"GET\"] = \"get\";\n  Actions[\"REPLY\"] = \"reply\";\n  Actions[\"EMIT\"] = \"emit\";\n  Actions[\"ERROR\"] = \"error\";\n})(Actions || (Actions = {}));\nfunction isGet(message) {\n  return message.switchboardAction === Actions.GET;\n}\nfunction isReply(message) {\n  return message.switchboardAction === Actions.REPLY;\n}\nfunction isEmit(message) {\n  return message.switchboardAction === Actions.EMIT;\n}\nfunction isError(message) {\n  return message.switchboardAction === Actions.ERROR;\n};(function () {var reactHotLoader = typeof reactHotLoaderGlobal !== 'undefined' ? reactHotLoaderGlobal.default : undefined;if (!reactHotLoader) {return;}reactHotLoader.register(Switchboard, \"Switchboard\", \"/Users/chenming/PycharmProjects/superset/superset-frontend/packages/superset-ui-switchboard/src/switchboard.ts\");reactHotLoader.register(Actions, \"Actions\", \"/Users/chenming/PycharmProjects/superset/superset-frontend/packages/superset-ui-switchboard/src/switchboard.ts\");reactHotLoader.register(isGet, \"isGet\", \"/Users/chenming/PycharmProjects/superset/superset-frontend/packages/superset-ui-switchboard/src/switchboard.ts\");reactHotLoader.register(isReply, \"isReply\", \"/Users/chenming/PycharmProjects/superset/superset-frontend/packages/superset-ui-switchboard/src/switchboard.ts\");reactHotLoader.register(isEmit, \"isEmit\", \"/Users/chenming/PycharmProjects/superset/superset-frontend/packages/superset-ui-switchboard/src/switchboard.ts\");reactHotLoader.register(isError, \"isError\", \"/Users/chenming/PycharmProjects/superset/superset-frontend/packages/superset-ui-switchboard/src/switchboard.ts\");})();;(function () {var leaveModule = typeof reactHotLoaderGlobal !== 'undefined' ? reactHotLoaderGlobal.leaveModule : undefined;leaveModule && leaveModule(module);})();//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9wYWNrYWdlcy9zdXBlcnNldC11aS1zd2l0Y2hib2FyZC9zcmMvc3dpdGNoYm9hcmQudHMuanMiLCJtYXBwaW5ncyI6Ijs7OztBQUFBOzs7Ozs7Ozs7Ozs7Ozs7OztBQWlCQTtBQVFBOzs7Ozs7QUFNQTtBQUNBOzs7O0FBT0E7OztBQUtBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFBQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUVBO0FBS0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFFQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUVBOzs7Ozs7Ozs7Ozs7OztBQWNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUFBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBRUE7Ozs7OztBQU1BO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBekpBO0FBQUE7QUErSkE7QUFBQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFlQTtBQUNBO0FBQ0E7QUFRQTtBQUNBO0FBQ0E7QUFRQTtBQUNBO0FBQ0E7QUFRQTtBQUNBO0FBQ0EiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9zdXBlcnNldC8uL3BhY2thZ2VzL3N1cGVyc2V0LXVpLXN3aXRjaGJvYXJkL3NyYy9zd2l0Y2hib2FyZC50cz9hMjU1Il0sInNvdXJjZXNDb250ZW50IjpbIi8qXG4gKiBMaWNlbnNlZCB0byB0aGUgQXBhY2hlIFNvZnR3YXJlIEZvdW5kYXRpb24gKEFTRikgdW5kZXIgb25lXG4gKiBvciBtb3JlIGNvbnRyaWJ1dG9yIGxpY2Vuc2UgYWdyZWVtZW50cy4gIFNlZSB0aGUgTk9USUNFIGZpbGVcbiAqIGRpc3RyaWJ1dGVkIHdpdGggdGhpcyB3b3JrIGZvciBhZGRpdGlvbmFsIGluZm9ybWF0aW9uXG4gKiByZWdhcmRpbmcgY29weXJpZ2h0IG93bmVyc2hpcC4gIFRoZSBBU0YgbGljZW5zZXMgdGhpcyBmaWxlXG4gKiB0byB5b3UgdW5kZXIgdGhlIEFwYWNoZSBMaWNlbnNlLCBWZXJzaW9uIDIuMCAodGhlXG4gKiBcIkxpY2Vuc2VcIik7IHlvdSBtYXkgbm90IHVzZSB0aGlzIGZpbGUgZXhjZXB0IGluIGNvbXBsaWFuY2VcbiAqIHdpdGggdGhlIExpY2Vuc2UuICBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXRcbiAqXG4gKiAgIGh0dHA6Ly93d3cuYXBhY2hlLm9yZy9saWNlbnNlcy9MSUNFTlNFLTIuMFxuICpcbiAqIFVubGVzcyByZXF1aXJlZCBieSBhcHBsaWNhYmxlIGxhdyBvciBhZ3JlZWQgdG8gaW4gd3JpdGluZyxcbiAqIHNvZnR3YXJlIGRpc3RyaWJ1dGVkIHVuZGVyIHRoZSBMaWNlbnNlIGlzIGRpc3RyaWJ1dGVkIG9uIGFuXG4gKiBcIkFTIElTXCIgQkFTSVMsIFdJVEhPVVQgV0FSUkFOVElFUyBPUiBDT05ESVRJT05TIE9GIEFOWVxuICogS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4gIFNlZSB0aGUgTGljZW5zZSBmb3IgdGhlXG4gKiBzcGVjaWZpYyBsYW5ndWFnZSBnb3Zlcm5pbmcgcGVybWlzc2lvbnMgYW5kIGxpbWl0YXRpb25zXG4gKiB1bmRlciB0aGUgTGljZW5zZS5cbiAqL1xuXG5leHBvcnQgdHlwZSBQYXJhbXMgPSB7XG4gIHBvcnQ6IE1lc3NhZ2VQb3J0O1xuICBuYW1lPzogc3RyaW5nO1xuICBkZWJ1Zz86IGJvb2xlYW47XG59O1xuXG4vKipcbiAqIEEgdXRpbGl0eSBmb3IgY29tbXVuaWNhdGlvbnMgYmV0d2VlbiBhbiBpZnJhbWUgYW5kIGl0cyBwYXJlbnQsIHVzZWQgYnkgdGhlIFN1cGVyc2V0IGVtYmVkZGVkIFNESy5cbiAqIFRoaXMgYnVpbGRzIHVzZWZ1bCBwYXR0ZXJucyBvbiB0b3Agb2YgdGhlIGJhc2ljIGZ1bmN0aW9uYWxpdHkgb2ZmZXJlZCBieSBNZXNzYWdlQ2hhbm5lbC5cbiAqXG4gKiBCb3RoIHdpbmRvd3MgaW5zdGFudGlhdGUgYSBTd2l0Y2hib2FyZCwgcGFzc2luZyBpbiB0aGVpciBNZXNzYWdlUG9ydHMuXG4gKiBDYWxsaW5nIG1ldGhvZHMgb24gdGhlIHN3aXRjaGJvYXJkIGNhdXNlcyBtZXNzYWdlcyB0byBiZSBzZW50IHRocm91Z2ggdGhlIGNoYW5uZWwuXG4gKi9cbmV4cG9ydCBjbGFzcyBTd2l0Y2hib2FyZCB7XG4gIHBvcnQ6IE1lc3NhZ2VQb3J0O1xuXG4gIG5hbWU6IHN0cmluZztcblxuICBtZXRob2RzOiBSZWNvcmQ8c3RyaW5nLCBNZXRob2Q8YW55LCB1bmtub3duPj4gPSB7fTtcblxuICAvLyB1c2VkIHRvIG1ha2UgdW5pcXVlIGlkc1xuICBpbmNyZW1lbnRvciA9IDE7XG5cbiAgZGVidWdNb2RlOiBib29sZWFuO1xuXG4gIGNvbnN0cnVjdG9yKHsgcG9ydCwgbmFtZSA9ICdzd2l0Y2hib2FyZCcsIGRlYnVnID0gZmFsc2UgfTogUGFyYW1zKSB7XG4gICAgdGhpcy5wb3J0ID0gcG9ydDtcbiAgICB0aGlzLm5hbWUgPSBuYW1lO1xuICAgIHRoaXMuZGVidWdNb2RlID0gZGVidWc7XG5cbiAgICBwb3J0LmFkZEV2ZW50TGlzdGVuZXIoJ21lc3NhZ2UnLCBhc3luYyBldmVudCA9PiB7XG4gICAgICB0aGlzLmxvZygnbWVzc2FnZSByZWNlaXZlZCcsIGV2ZW50KTtcbiAgICAgIGNvbnN0IG1lc3NhZ2UgPSBldmVudC5kYXRhO1xuICAgICAgaWYgKGlzR2V0KG1lc3NhZ2UpKSB7XG4gICAgICAgIC8vIGZpbmQgdGhlIG1ldGhvZCwgY2FsbCBpdCwgYW5kIHJlcGx5IHdpdGggdGhlIHJlc3VsdFxuICAgICAgICB0aGlzLnBvcnQucG9zdE1lc3NhZ2UoYXdhaXQgdGhpcy5nZXRNZXRob2RSZXN1bHQobWVzc2FnZSkpO1xuICAgICAgfSBlbHNlIGlmIChpc0VtaXQobWVzc2FnZSkpIHtcbiAgICAgICAgY29uc3QgeyBtZXRob2QsIGFyZ3MgfSA9IG1lc3NhZ2U7XG4gICAgICAgIC8vIEZpbmQgdGhlIG1ldGhvZCBhbmQgY2FsbCBpdCwgYnV0IG5vIHJlc3VsdCBuZWNlc3NhcnkuXG4gICAgICAgIC8vIFNob3VsZCB0aGlzIG11bHRpY2FzdCB0byBhIHNldCBvZiBsaXN0ZW5lcnM/XG4gICAgICAgIC8vIE1heWJlLCBidXQgdGhhdCByZXF1aXJlcyB3cml0aW5nIGEgYnVuY2ggbW9yZSBjb2RlXG4gICAgICAgIC8vIGFuZCBJIGhhdmVuJ3QgZm91bmQgYSBuZWVkIGZvciBpdCB5ZXQuXG4gICAgICAgIGNvbnN0IGV4ZWN1dG9yID0gdGhpcy5tZXRob2RzW21ldGhvZF07XG4gICAgICAgIGlmIChleGVjdXRvcikge1xuICAgICAgICAgIGV4ZWN1dG9yKGFyZ3MpO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfSk7XG4gIH1cblxuICBwcml2YXRlIGFzeW5jIGdldE1ldGhvZFJlc3VsdCh7XG4gICAgbWVzc2FnZUlkLFxuICAgIG1ldGhvZCxcbiAgICBhcmdzLFxuICB9OiBHZXRNZXNzYWdlKTogUHJvbWlzZTxSZXBseU1lc3NhZ2UgfCBFcnJvck1lc3NhZ2U+IHtcbiAgICBjb25zdCBleGVjdXRvciA9IHRoaXMubWV0aG9kc1ttZXRob2RdO1xuICAgIGlmIChleGVjdXRvciA9PSBudWxsKSB7XG4gICAgICByZXR1cm4gPEVycm9yTWVzc2FnZT57XG4gICAgICAgIHN3aXRjaGJvYXJkQWN0aW9uOiBBY3Rpb25zLkVSUk9SLFxuICAgICAgICBtZXNzYWdlSWQsXG4gICAgICAgIGVycm9yOiBgWyR7dGhpcy5uYW1lfV0gTWV0aG9kIFwiJHttZXRob2R9XCIgaXMgbm90IGRlZmluZWRgLFxuICAgICAgfTtcbiAgICB9XG4gICAgdHJ5IHtcbiAgICAgIGNvbnN0IHJlc3VsdCA9IGF3YWl0IGV4ZWN1dG9yKGFyZ3MpO1xuICAgICAgcmV0dXJuIDxSZXBseU1lc3NhZ2U+e1xuICAgICAgICBzd2l0Y2hib2FyZEFjdGlvbjogQWN0aW9ucy5SRVBMWSxcbiAgICAgICAgbWVzc2FnZUlkLFxuICAgICAgICByZXN1bHQsXG4gICAgICB9O1xuICAgIH0gY2F0Y2ggKGVycikge1xuICAgICAgdGhpcy5sb2dFcnJvcihlcnIpO1xuICAgICAgcmV0dXJuIDxFcnJvck1lc3NhZ2U+e1xuICAgICAgICBzd2l0Y2hib2FyZEFjdGlvbjogQWN0aW9ucy5FUlJPUixcbiAgICAgICAgbWVzc2FnZUlkLFxuICAgICAgICBlcnJvcjogYFske3RoaXMubmFtZX1dIE1ldGhvZCBcIiR7bWV0aG9kfVwiIHRocmV3IGFuIGVycm9yYCxcbiAgICAgIH07XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIERlZmluZXMgYSBtZXRob2QgdGhhdCBjYW4gYmUgXCJjYWxsZWRcIiBmcm9tIHRoZSBvdGhlciBzaWRlIGJ5IHNlbmRpbmcgYW4gZXZlbnQuXG4gICAqL1xuICBkZWZpbmVNZXRob2Q8QSA9IGFueSwgUiA9IGFueT4obWV0aG9kTmFtZTogc3RyaW5nLCBleGVjdXRvcjogTWV0aG9kPEEsIFI+KSB7XG4gICAgdGhpcy5tZXRob2RzW21ldGhvZE5hbWVdID0gZXhlY3V0b3I7XG4gIH1cblxuICAvKipcbiAgICogQ2FsbHMgYSBtZXRob2QgcmVnaXN0ZXJlZCBvbiB0aGUgb3RoZXIgc2lkZSwgYW5kIHJldHVybnMgdGhlIHJlc3VsdC5cbiAgICpcbiAgICogSG93IHRoaXMgaXMgYWNjb21wbGlzaGVkOlxuICAgKiBUaGlzIHN3aXRjaGJvYXJkIHNlbmRzIGEgXCJnZXRcIiBtZXNzYWdlIG92ZXIgdGhlIGNoYW5uZWwgZGVzY3JpYmluZyB3aGljaCBtZXRob2QgdG8gY2FsbCB3aXRoIHdoaWNoIGFyZ3VtZW50cy5cbiAgICogVGhlIG90aGVyIHNpZGUncyBzd2l0Y2hib2FyZCBmaW5kcyBhIG1ldGhvZCB3aXRoIHRoYXQgbmFtZSwgYW5kIGNhbGxzIGl0IHdpdGggdGhlIGFyZ3VtZW50cy5cbiAgICogSXQgdGhlbiBwYWNrYWdlcyB1cCB0aGUgcmV0dXJuZWQgdmFsdWUgaW50byBhIFwicmVwbHlcIiBtZXNzYWdlLCBzZW5kaW5nIGl0IGJhY2sgdG8gdXMgYWNyb3NzIHRoZSBjaGFubmVsLlxuICAgKiBUaGlzIHN3aXRjaGJvYXJkIGhhcyBhdHRhY2hlZCBhIGxpc3RlbmVyIG9uIHRoZSBjaGFubmVsLCB3aGljaCB3aWxsIHJlc29sdmUgd2l0aCB0aGUgcmVzdWx0IHdoZW4gYSByZXBseSBpcyBkZXRlY3RlZC5cbiAgICpcbiAgICogSW5zdGVhZCBvZiBhbiBhcmd1bWVudHMgbGlzdCwgYXJndW1lbnRzIGFyZSBzdXBwbGllZCBhcyBhIG1hcC5cbiAgICpcbiAgICogQHBhcmFtIG1ldGhvZCB0aGUgbmFtZSBvZiB0aGUgbWV0aG9kIHRvIGNhbGxcbiAgICogQHBhcmFtIGFyZ3MgYXJndW1lbnRzIHRoYXQgd2lsbCBiZSBzdXBwbGllZC4gTXVzdCBiZSBzZXJpYWxpemFibGUsIG5vIGZ1bmN0aW9ucyBvciBvdGhlciBub25lbnNlLlxuICAgKiBAcmV0dXJucyB3aGF0ZXZlciBpcyByZXR1cm5lZCBmcm9tIHRoZSBtZXRob2RcbiAgICovXG4gIGdldDxUID0gdW5rbm93bj4obWV0aG9kOiBzdHJpbmcsIGFyZ3M6IHVua25vd24gPSB1bmRlZmluZWQpOiBQcm9taXNlPFQ+IHtcbiAgICByZXR1cm4gbmV3IFByb21pc2UoKHJlc29sdmUsIHJlamVjdCkgPT4ge1xuICAgICAgLy8gSW4gb3JkZXIgdG8gXCJjYWxsIGEgbWV0aG9kXCIgb24gdGhlIG90aGVyIHNpZGUgb2YgdGhlIHBvcnQsXG4gICAgICAvLyB3ZSB3aWxsIHNlbmQgYSBtZXNzYWdlIHdpdGggYSB1bmlxdWUgaWRcbiAgICAgIGNvbnN0IG1lc3NhZ2VJZCA9IHRoaXMuZ2V0TmV3TWVzc2FnZUlkKCk7XG4gICAgICAvLyBhdHRhY2ggYSBuZXcgbGlzdGVuZXIgdG8gb3VyIHBvcnQsIGFuZCByZW1vdmUgaXQgd2hlbiB3ZSBnZXQgYSByZXNwb25zZVxuICAgICAgY29uc3QgbGlzdGVuZXIgPSAoZXZlbnQ6IE1lc3NhZ2VFdmVudCkgPT4ge1xuICAgICAgICBjb25zdCBtZXNzYWdlID0gZXZlbnQuZGF0YTtcbiAgICAgICAgaWYgKG1lc3NhZ2UubWVzc2FnZUlkICE9PSBtZXNzYWdlSWQpIHJldHVybjtcbiAgICAgICAgdGhpcy5wb3J0LnJlbW92ZUV2ZW50TGlzdGVuZXIoJ21lc3NhZ2UnLCBsaXN0ZW5lcik7XG4gICAgICAgIGlmIChpc1JlcGx5KG1lc3NhZ2UpKSB7XG4gICAgICAgICAgcmVzb2x2ZShtZXNzYWdlLnJlc3VsdCk7XG4gICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgY29uc3QgZXJyU3RyID0gaXNFcnJvcihtZXNzYWdlKVxuICAgICAgICAgICAgPyBtZXNzYWdlLmVycm9yXG4gICAgICAgICAgICA6ICdVbmV4cGVjdGVkIHJlc3BvbnNlIG1lc3NhZ2UnO1xuICAgICAgICAgIHJlamVjdChuZXcgRXJyb3IoZXJyU3RyKSk7XG4gICAgICAgIH1cbiAgICAgIH07XG4gICAgICB0aGlzLnBvcnQuYWRkRXZlbnRMaXN0ZW5lcignbWVzc2FnZScsIGxpc3RlbmVyKTtcbiAgICAgIHRoaXMucG9ydC5zdGFydCgpO1xuICAgICAgY29uc3QgbWVzc2FnZTogR2V0TWVzc2FnZSA9IHtcbiAgICAgICAgc3dpdGNoYm9hcmRBY3Rpb246IEFjdGlvbnMuR0VULFxuICAgICAgICBtZXRob2QsXG4gICAgICAgIG1lc3NhZ2VJZCxcbiAgICAgICAgYXJncyxcbiAgICAgIH07XG4gICAgICB0aGlzLnBvcnQucG9zdE1lc3NhZ2UobWVzc2FnZSk7XG4gICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogRW1pdCBjYWxscyBhIG1ldGhvZCBvbiB0aGUgb3RoZXIgc2lkZSBqdXN0IGxpa2UgZ2V0IGRvZXMuXG4gICAqIEJ1dCBlbWl0IGRvZXNuJ3Qgd2FpdCBmb3IgYSByZXNwb25zZSwgaXQganVzdCBzZW5kcyBhbmQgZm9yZ2V0cy5cbiAgICpcbiAgICogQHBhcmFtIG1ldGhvZFxuICAgKiBAcGFyYW0gYXJnc1xuICAgKi9cbiAgZW1pdChtZXRob2Q6IHN0cmluZywgYXJnczogdW5rbm93biA9IHVuZGVmaW5lZCkge1xuICAgIGNvbnN0IG1lc3NhZ2U6IEVtaXRNZXNzYWdlID0ge1xuICAgICAgc3dpdGNoYm9hcmRBY3Rpb246IEFjdGlvbnMuRU1JVCxcbiAgICAgIG1ldGhvZCxcbiAgICAgIGFyZ3MsXG4gICAgfTtcbiAgICB0aGlzLnBvcnQucG9zdE1lc3NhZ2UobWVzc2FnZSk7XG4gIH1cblxuICBzdGFydCgpIHtcbiAgICB0aGlzLnBvcnQuc3RhcnQoKTtcbiAgfVxuXG4gIHByaXZhdGUgbG9nKC4uLmFyZ3M6IHVua25vd25bXSkge1xuICAgIGlmICh0aGlzLmRlYnVnTW9kZSkge1xuICAgICAgY29uc29sZS5kZWJ1ZyhgWyR7dGhpcy5uYW1lfV1gLCAuLi5hcmdzKTtcbiAgICB9XG4gIH1cblxuICBwcml2YXRlIGxvZ0Vycm9yKC4uLmFyZ3M6IHVua25vd25bXSkge1xuICAgIGNvbnNvbGUuZXJyb3IoYFske3RoaXMubmFtZX1dYCwgLi4uYXJncyk7XG4gIH1cblxuICBwcml2YXRlIGdldE5ld01lc3NhZ2VJZCgpIHtcbiAgICAvLyBlc2xpbnQtZGlzYWJsZS1uZXh0LWxpbmUgbm8tcGx1c3BsdXNcbiAgICByZXR1cm4gYG1fJHt0aGlzLm5hbWV9XyR7dGhpcy5pbmNyZW1lbnRvcisrfWA7XG4gIH1cbn1cblxudHlwZSBNZXRob2Q8QSBleHRlbmRzIHt9LCBSPiA9IChhcmdzOiBBKSA9PiBSIHwgUHJvbWlzZTxSPjtcblxuLy8gRWFjaCBtZXNzYWdlIHdlIHNlbmQgb24gdGhlIGNoYW5uZWwgc3BlY2lmaWVzIGFuIGFjdGlvbiB3ZSB3YW50IHRoZSBvdGhlciBzaWRlIHRvIGNvb3BlcmF0ZSB3aXRoLlxuZW51bSBBY3Rpb25zIHtcbiAgR0VUID0gJ2dldCcsXG4gIFJFUExZID0gJ3JlcGx5JyxcbiAgRU1JVCA9ICdlbWl0JyxcbiAgRVJST1IgPSAnZXJyb3InLFxufVxuXG4vLyBoZWxwZXIgdHlwZXMvZnVuY3Rpb25zIGZvciBtYWtpbmcgc3VyZSB3aXJlcyBkb24ndCBnZXQgY3Jvc3NlZFxuXG5pbnRlcmZhY2UgTWVzc2FnZSB7XG4gIHN3aXRjaGJvYXJkQWN0aW9uOiBBY3Rpb25zO1xufVxuXG5pbnRlcmZhY2UgR2V0TWVzc2FnZTxUID0gYW55PiBleHRlbmRzIE1lc3NhZ2Uge1xuICBzd2l0Y2hib2FyZEFjdGlvbjogQWN0aW9ucy5HRVQ7XG4gIG1ldGhvZDogc3RyaW5nO1xuICBtZXNzYWdlSWQ6IHN0cmluZztcbiAgYXJnczogVDtcbn1cblxuZnVuY3Rpb24gaXNHZXQobWVzc2FnZTogTWVzc2FnZSk6IG1lc3NhZ2UgaXMgR2V0TWVzc2FnZSB7XG4gIHJldHVybiBtZXNzYWdlLnN3aXRjaGJvYXJkQWN0aW9uID09PSBBY3Rpb25zLkdFVDtcbn1cblxuaW50ZXJmYWNlIFJlcGx5TWVzc2FnZTxUID0gYW55PiBleHRlbmRzIE1lc3NhZ2Uge1xuICBzd2l0Y2hib2FyZEFjdGlvbjogQWN0aW9ucy5SRVBMWTtcbiAgbWVzc2FnZUlkOiBzdHJpbmc7XG4gIHJlc3VsdDogVDtcbn1cblxuZnVuY3Rpb24gaXNSZXBseShtZXNzYWdlOiBNZXNzYWdlKTogbWVzc2FnZSBpcyBSZXBseU1lc3NhZ2Uge1xuICByZXR1cm4gbWVzc2FnZS5zd2l0Y2hib2FyZEFjdGlvbiA9PT0gQWN0aW9ucy5SRVBMWTtcbn1cblxuaW50ZXJmYWNlIEVtaXRNZXNzYWdlPFQgPSBhbnk+IGV4dGVuZHMgTWVzc2FnZSB7XG4gIHN3aXRjaGJvYXJkQWN0aW9uOiBBY3Rpb25zLkVNSVQ7XG4gIG1ldGhvZDogc3RyaW5nO1xuICBhcmdzOiBUO1xufVxuXG5mdW5jdGlvbiBpc0VtaXQobWVzc2FnZTogTWVzc2FnZSk6IG1lc3NhZ2UgaXMgRW1pdE1lc3NhZ2Uge1xuICByZXR1cm4gbWVzc2FnZS5zd2l0Y2hib2FyZEFjdGlvbiA9PT0gQWN0aW9ucy5FTUlUO1xufVxuXG5pbnRlcmZhY2UgRXJyb3JNZXNzYWdlIGV4dGVuZHMgTWVzc2FnZSB7XG4gIHN3aXRjaGJvYXJkQWN0aW9uOiBBY3Rpb25zLkVSUk9SO1xuICBtZXNzYWdlSWQ6IHN0cmluZztcbiAgZXJyb3I6IHN0cmluZztcbn1cblxuZnVuY3Rpb24gaXNFcnJvcihtZXNzYWdlOiBNZXNzYWdlKTogbWVzc2FnZSBpcyBFcnJvck1lc3NhZ2Uge1xuICByZXR1cm4gbWVzc2FnZS5zd2l0Y2hib2FyZEFjdGlvbiA9PT0gQWN0aW9ucy5FUlJPUjtcbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///./packages/superset-ui-switchboard/src/switchboard.ts\n");

/***/ }),

/***/ "./src/embedded/index.tsx":
/*!********************************!*\
  !*** ./src/embedded/index.tsx ***!
  \********************************/
/***/ ((module, __unused_webpack___webpack_exports__, __webpack_require__) => {

eval("/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ \"./node_modules/react/index.js\");\n/* harmony import */ var react_dom__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-dom */ \"./node_modules/react-dom/index.js\");\n/* harmony import */ var react_dom__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_dom__WEBPACK_IMPORTED_MODULE_1__);\n/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! react-router-dom */ \"./node_modules/react-router-dom/esm/react-router-dom.js\");\n/* harmony import */ var react_router_dom__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! react-router-dom */ \"./node_modules/react-router/esm/react-router.js\");\n/* harmony import */ var _superset_ui_switchboard__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @superset-ui/switchboard */ \"./packages/superset-ui-switchboard/src/switchboard.ts\");\n/* harmony import */ var src_preamble__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! src/preamble */ \"./src/preamble.ts\");\n/* harmony import */ var src_setup_setupClient__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! src/setup/setupClient */ \"./src/setup/setupClient.ts\");\n/* harmony import */ var src_views_RootContextProviders__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! src/views/RootContextProviders */ \"./src/views/RootContextProviders.tsx\");\n/* harmony import */ var src_components_ErrorBoundary__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! src/components/ErrorBoundary */ \"./src/components/ErrorBoundary/index.jsx\");\n/* harmony import */ var src_components_Loading__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! src/components/Loading */ \"./src/components/Loading/index.tsx\");\n/* harmony import */ var _emotion_react__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @emotion/react */ \"./node_modules/@emotion/react/dist/emotion-react.browser.esm.js\");\n/* module decorator */ module = __webpack_require__.hmd(module);\n(function () {var enterModule = typeof reactHotLoaderGlobal !== 'undefined' ? reactHotLoaderGlobal.enterModule : undefined;enterModule && enterModule(module);})();var __signature__ = typeof reactHotLoaderGlobal !== 'undefined' ? reactHotLoaderGlobal.default.signature : function (a) {return a;}; /**\n * Licensed to the Apache Software Foundation (ASF) under one\n * or more contributor license agreements.  See the NOTICE file\n * distributed with this work for additional information\n * regarding copyright ownership.  The ASF licenses this file\n * to you under the Apache License, Version 2.0 (the\n * \"License\"); you may not use this file except in compliance\n * with the License.  You may obtain a copy of the License at\n *\n *   http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing,\n * software distributed under the License is distributed on an\n * \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY\n * KIND, either express or implied.  See the License for the\n * specific language governing permissions and limitations\n * under the License.\n */\n\n\n\n\n\n\n\n\n\nconst debugMode = \"development\" === 'development';\nfunction log(...info) {\n  if (debugMode) {\n    console.debug(`[superset]`, ...info);\n  }\n}\nconst LazyDashboardPage = /*#__PURE__*/(0,react__WEBPACK_IMPORTED_MODULE_0__.lazy)(() => Promise.all(/*! import() | DashboardPage */[__webpack_require__.e(\"vendors\"), __webpack_require__.e(\"thumbnail\"), __webpack_require__.e(\"vendors-node_modules_d3-tip_index_js-node_modules_dompurify_dist_purify_js-node_modules_echar-a756c7\"), __webpack_require__.e(\"src_setup_setupPlugins_ts\"), __webpack_require__.e(\"DashboardPage\")]).then(__webpack_require__.bind(__webpack_require__, /*! src/dashboard/containers/DashboardPage */ \"./src/dashboard/containers/DashboardPage.tsx\")));\nconst EmbeddedApp = () => (0,_emotion_react__WEBPACK_IMPORTED_MODULE_7__.jsx)(react_router_dom__WEBPACK_IMPORTED_MODULE_8__.BrowserRouter, null,\n(0,_emotion_react__WEBPACK_IMPORTED_MODULE_7__.jsx)(react_router_dom__WEBPACK_IMPORTED_MODULE_9__.Route, { path: \"/dashboard/:idOrSlug/embedded\" },\n(0,_emotion_react__WEBPACK_IMPORTED_MODULE_7__.jsx)(react__WEBPACK_IMPORTED_MODULE_0__.Suspense, { fallback: (0,_emotion_react__WEBPACK_IMPORTED_MODULE_7__.jsx)(src_components_Loading__WEBPACK_IMPORTED_MODULE_6__[\"default\"], null) },\n(0,_emotion_react__WEBPACK_IMPORTED_MODULE_7__.jsx)(src_views_RootContextProviders__WEBPACK_IMPORTED_MODULE_4__.RootContextProviders, null,\n(0,_emotion_react__WEBPACK_IMPORTED_MODULE_7__.jsx)(src_components_ErrorBoundary__WEBPACK_IMPORTED_MODULE_5__[\"default\"], null,\n(0,_emotion_react__WEBPACK_IMPORTED_MODULE_7__.jsx)(LazyDashboardPage, null))))));\n\n\n\n\n\nconst appMountPoint = document.getElementById('app');\nconst MESSAGE_TYPE = '__embedded_comms__';\nif (!window.parent) {\n  appMountPoint.innerHTML =\n  'This page is intended to be embedded in an iframe, but no window.parent was found.';\n}\n// if the page is embedded in an origin that hasn't\n// been authorized by the curator, we forbid access entirely.\n// todo: check the referrer on the route serving this page instead\n// const ALLOW_ORIGINS = ['http://127.0.0.1:9001', 'http://localhost:9001'];\n// const parentOrigin = new URL(document.referrer).origin;\n// if (!ALLOW_ORIGINS.includes(parentOrigin)) {\n//   throw new Error(\n//     `[superset] iframe parent ${parentOrigin} is not in the list of allowed origins`,\n//   );\n// }\nasync function start(guestToken) {var _bootstrapData$config;\n  // the preamble configures a client, but we need to configure a new one\n  // now that we have the guest token\n  (0,src_setup_setupClient__WEBPACK_IMPORTED_MODULE_3__[\"default\"])({\n    guestToken,\n    guestTokenHeaderName: (_bootstrapData$config = src_preamble__WEBPACK_IMPORTED_MODULE_2__.bootstrapData.config) == null ? void 0 : _bootstrapData$config.GUEST_TOKEN_HEADER_NAME });\n\n  react_dom__WEBPACK_IMPORTED_MODULE_1___default().render((0,_emotion_react__WEBPACK_IMPORTED_MODULE_7__.jsx)(EmbeddedApp, null), appMountPoint);\n}\nfunction validateMessageEvent(event) {var _event$data, _event$data2;\n  if (((_event$data = event.data) == null ? void 0 : _event$data.type) === 'webpackClose' ||\n  ((_event$data2 = event.data) == null ? void 0 : _event$data2.source) === '@devtools-page') {\n    // sometimes devtools use the messaging api and we want to ignore those\n    throw new Error(\"Sir, this is a Wendy's\");\n  }\n  // if (!ALLOW_ORIGINS.includes(event.origin)) {\n  //   throw new Error('Message origin is not in the allowed list');\n  // }\n  if (typeof event.data !== 'object' || event.data.type !== MESSAGE_TYPE) {\n    throw new Error(`Message type does not match type used for embedded comms`);\n  }\n}\nwindow.addEventListener('message', function (event) {var _event$ports;\n  try {\n    validateMessageEvent(event);\n  }\n  catch (err) {\n    log('ignoring message', err, event);\n    return;\n  }\n  const port = (_event$ports = event.ports) == null ? void 0 : _event$ports[0];\n  if (event.data.handshake === 'port transfer' && port) {\n    log('message port received', event);\n    const switchboard = new _superset_ui_switchboard__WEBPACK_IMPORTED_MODULE_10__.Switchboard({\n      port,\n      name: 'superset',\n      debug: debugMode });\n\n    switchboard.defineMethod('guestToken', ({ guestToken }) => {\n      start(guestToken);\n    });\n    switchboard.defineMethod('getScrollSize', () => ({\n      width: document.body.scrollWidth,\n      height: document.body.scrollHeight }));\n\n    switchboard.start();\n  }\n});\nlog('embed page is ready to receive messages');;(function () {var reactHotLoader = typeof reactHotLoaderGlobal !== 'undefined' ? reactHotLoaderGlobal.default : undefined;if (!reactHotLoader) {return;}reactHotLoader.register(debugMode, \"debugMode\", \"/Users/chenming/PycharmProjects/superset/superset-frontend/src/embedded/index.tsx\");reactHotLoader.register(log, \"log\", \"/Users/chenming/PycharmProjects/superset/superset-frontend/src/embedded/index.tsx\");reactHotLoader.register(LazyDashboardPage, \"LazyDashboardPage\", \"/Users/chenming/PycharmProjects/superset/superset-frontend/src/embedded/index.tsx\");reactHotLoader.register(EmbeddedApp, \"EmbeddedApp\", \"/Users/chenming/PycharmProjects/superset/superset-frontend/src/embedded/index.tsx\");reactHotLoader.register(appMountPoint, \"appMountPoint\", \"/Users/chenming/PycharmProjects/superset/superset-frontend/src/embedded/index.tsx\");reactHotLoader.register(MESSAGE_TYPE, \"MESSAGE_TYPE\", \"/Users/chenming/PycharmProjects/superset/superset-frontend/src/embedded/index.tsx\");reactHotLoader.register(start, \"start\", \"/Users/chenming/PycharmProjects/superset/superset-frontend/src/embedded/index.tsx\");reactHotLoader.register(validateMessageEvent, \"validateMessageEvent\", \"/Users/chenming/PycharmProjects/superset/superset-frontend/src/embedded/index.tsx\");})();;(function () {var leaveModule = typeof reactHotLoaderGlobal !== 'undefined' ? reactHotLoaderGlobal.leaveModule : undefined;leaveModule && leaveModule(module);})();//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvZW1iZWRkZWQvaW5kZXgudHN4LmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7QUFBQTs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFpQkE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQU9BO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7Ozs7O0FBUUE7QUFFQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUVBO0FBQ0E7QUFFQTtBQUVBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFBQTtBQUNBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUNBOztBQUdBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTs7QUFHQTtBQUNBO0FBQ0E7QUFFQSIsInNvdXJjZXMiOlsid2VicGFjazovL3N1cGVyc2V0Ly4vc3JjL2VtYmVkZGVkL2luZGV4LnRzeD80NjY2Il0sInNvdXJjZXNDb250ZW50IjpbIi8qKlxuICogTGljZW5zZWQgdG8gdGhlIEFwYWNoZSBTb2Z0d2FyZSBGb3VuZGF0aW9uIChBU0YpIHVuZGVyIG9uZVxuICogb3IgbW9yZSBjb250cmlidXRvciBsaWNlbnNlIGFncmVlbWVudHMuICBTZWUgdGhlIE5PVElDRSBmaWxlXG4gKiBkaXN0cmlidXRlZCB3aXRoIHRoaXMgd29yayBmb3IgYWRkaXRpb25hbCBpbmZvcm1hdGlvblxuICogcmVnYXJkaW5nIGNvcHlyaWdodCBvd25lcnNoaXAuICBUaGUgQVNGIGxpY2Vuc2VzIHRoaXMgZmlsZVxuICogdG8geW91IHVuZGVyIHRoZSBBcGFjaGUgTGljZW5zZSwgVmVyc2lvbiAyLjAgKHRoZVxuICogXCJMaWNlbnNlXCIpOyB5b3UgbWF5IG5vdCB1c2UgdGhpcyBmaWxlIGV4Y2VwdCBpbiBjb21wbGlhbmNlXG4gKiB3aXRoIHRoZSBMaWNlbnNlLiAgWW91IG1heSBvYnRhaW4gYSBjb3B5IG9mIHRoZSBMaWNlbnNlIGF0XG4gKlxuICogICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjBcbiAqXG4gKiBVbmxlc3MgcmVxdWlyZWQgYnkgYXBwbGljYWJsZSBsYXcgb3IgYWdyZWVkIHRvIGluIHdyaXRpbmcsXG4gKiBzb2Z0d2FyZSBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhblxuICogXCJBUyBJU1wiIEJBU0lTLCBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTllcbiAqIEtJTkQsIGVpdGhlciBleHByZXNzIG9yIGltcGxpZWQuICBTZWUgdGhlIExpY2Vuc2UgZm9yIHRoZVxuICogc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZCBsaW1pdGF0aW9uc1xuICogdW5kZXIgdGhlIExpY2Vuc2UuXG4gKi9cbmltcG9ydCBSZWFjdCwgeyBsYXp5LCBTdXNwZW5zZSB9IGZyb20gJ3JlYWN0JztcbmltcG9ydCBSZWFjdERPTSBmcm9tICdyZWFjdC1kb20nO1xuaW1wb3J0IHsgQnJvd3NlclJvdXRlciBhcyBSb3V0ZXIsIFJvdXRlIH0gZnJvbSAncmVhY3Qtcm91dGVyLWRvbSc7XG5pbXBvcnQgeyBTd2l0Y2hib2FyZCB9IGZyb20gJ0BzdXBlcnNldC11aS9zd2l0Y2hib2FyZCc7XG5pbXBvcnQgeyBib290c3RyYXBEYXRhIH0gZnJvbSAnc3JjL3ByZWFtYmxlJztcbmltcG9ydCBzZXR1cENsaWVudCBmcm9tICdzcmMvc2V0dXAvc2V0dXBDbGllbnQnO1xuaW1wb3J0IHsgUm9vdENvbnRleHRQcm92aWRlcnMgfSBmcm9tICdzcmMvdmlld3MvUm9vdENvbnRleHRQcm92aWRlcnMnO1xuaW1wb3J0IEVycm9yQm91bmRhcnkgZnJvbSAnc3JjL2NvbXBvbmVudHMvRXJyb3JCb3VuZGFyeSc7XG5pbXBvcnQgTG9hZGluZyBmcm9tICdzcmMvY29tcG9uZW50cy9Mb2FkaW5nJztcblxuY29uc3QgZGVidWdNb2RlID0gcHJvY2Vzcy5lbnYuV0VCUEFDS19NT0RFID09PSAnZGV2ZWxvcG1lbnQnO1xuXG5mdW5jdGlvbiBsb2coLi4uaW5mbzogdW5rbm93bltdKSB7XG4gIGlmIChkZWJ1Z01vZGUpIHtcbiAgICBjb25zb2xlLmRlYnVnKGBbc3VwZXJzZXRdYCwgLi4uaW5mbyk7XG4gIH1cbn1cblxuY29uc3QgTGF6eURhc2hib2FyZFBhZ2UgPSBsYXp5KFxuICAoKSA9PlxuICAgIGltcG9ydChcbiAgICAgIC8qIHdlYnBhY2tDaHVua05hbWU6IFwiRGFzaGJvYXJkUGFnZVwiICovICdzcmMvZGFzaGJvYXJkL2NvbnRhaW5lcnMvRGFzaGJvYXJkUGFnZSdcbiAgICApLFxuKTtcblxuY29uc3QgRW1iZWRkZWRBcHAgPSAoKSA9PiAoXG4gIDxSb3V0ZXI+XG4gICAgPFJvdXRlIHBhdGg9XCIvZGFzaGJvYXJkLzppZE9yU2x1Zy9lbWJlZGRlZFwiPlxuICAgICAgPFN1c3BlbnNlIGZhbGxiYWNrPXs8TG9hZGluZyAvPn0+XG4gICAgICAgIDxSb290Q29udGV4dFByb3ZpZGVycz5cbiAgICAgICAgICA8RXJyb3JCb3VuZGFyeT5cbiAgICAgICAgICAgIDxMYXp5RGFzaGJvYXJkUGFnZSAvPlxuICAgICAgICAgIDwvRXJyb3JCb3VuZGFyeT5cbiAgICAgICAgPC9Sb290Q29udGV4dFByb3ZpZGVycz5cbiAgICAgIDwvU3VzcGVuc2U+XG4gICAgPC9Sb3V0ZT5cbiAgPC9Sb3V0ZXI+XG4pO1xuXG5jb25zdCBhcHBNb3VudFBvaW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2FwcCcpITtcblxuY29uc3QgTUVTU0FHRV9UWVBFID0gJ19fZW1iZWRkZWRfY29tbXNfXyc7XG5cbmlmICghd2luZG93LnBhcmVudCkge1xuICBhcHBNb3VudFBvaW50LmlubmVySFRNTCA9XG4gICAgJ1RoaXMgcGFnZSBpcyBpbnRlbmRlZCB0byBiZSBlbWJlZGRlZCBpbiBhbiBpZnJhbWUsIGJ1dCBubyB3aW5kb3cucGFyZW50IHdhcyBmb3VuZC4nO1xufVxuXG4vLyBpZiB0aGUgcGFnZSBpcyBlbWJlZGRlZCBpbiBhbiBvcmlnaW4gdGhhdCBoYXNuJ3Rcbi8vIGJlZW4gYXV0aG9yaXplZCBieSB0aGUgY3VyYXRvciwgd2UgZm9yYmlkIGFjY2VzcyBlbnRpcmVseS5cbi8vIHRvZG86IGNoZWNrIHRoZSByZWZlcnJlciBvbiB0aGUgcm91dGUgc2VydmluZyB0aGlzIHBhZ2UgaW5zdGVhZFxuLy8gY29uc3QgQUxMT1dfT1JJR0lOUyA9IFsnaHR0cDovLzEyNy4wLjAuMTo5MDAxJywgJ2h0dHA6Ly9sb2NhbGhvc3Q6OTAwMSddO1xuLy8gY29uc3QgcGFyZW50T3JpZ2luID0gbmV3IFVSTChkb2N1bWVudC5yZWZlcnJlcikub3JpZ2luO1xuLy8gaWYgKCFBTExPV19PUklHSU5TLmluY2x1ZGVzKHBhcmVudE9yaWdpbikpIHtcbi8vICAgdGhyb3cgbmV3IEVycm9yKFxuLy8gICAgIGBbc3VwZXJzZXRdIGlmcmFtZSBwYXJlbnQgJHtwYXJlbnRPcmlnaW59IGlzIG5vdCBpbiB0aGUgbGlzdCBvZiBhbGxvd2VkIG9yaWdpbnNgLFxuLy8gICApO1xuLy8gfVxuXG5hc3luYyBmdW5jdGlvbiBzdGFydChndWVzdFRva2VuOiBzdHJpbmcpIHtcbiAgLy8gdGhlIHByZWFtYmxlIGNvbmZpZ3VyZXMgYSBjbGllbnQsIGJ1dCB3ZSBuZWVkIHRvIGNvbmZpZ3VyZSBhIG5ldyBvbmVcbiAgLy8gbm93IHRoYXQgd2UgaGF2ZSB0aGUgZ3Vlc3QgdG9rZW5cbiAgc2V0dXBDbGllbnQoe1xuICAgIGd1ZXN0VG9rZW4sXG4gICAgZ3Vlc3RUb2tlbkhlYWRlck5hbWU6IGJvb3RzdHJhcERhdGEuY29uZmlnPy5HVUVTVF9UT0tFTl9IRUFERVJfTkFNRSxcbiAgfSk7XG4gIFJlYWN0RE9NLnJlbmRlcig8RW1iZWRkZWRBcHAgLz4sIGFwcE1vdW50UG9pbnQpO1xufVxuXG5mdW5jdGlvbiB2YWxpZGF0ZU1lc3NhZ2VFdmVudChldmVudDogTWVzc2FnZUV2ZW50KSB7XG4gIGlmIChcbiAgICBldmVudC5kYXRhPy50eXBlID09PSAnd2VicGFja0Nsb3NlJyB8fFxuICAgIGV2ZW50LmRhdGE/LnNvdXJjZSA9PT0gJ0BkZXZ0b29scy1wYWdlJ1xuICApIHtcbiAgICAvLyBzb21ldGltZXMgZGV2dG9vbHMgdXNlIHRoZSBtZXNzYWdpbmcgYXBpIGFuZCB3ZSB3YW50IHRvIGlnbm9yZSB0aG9zZVxuICAgIHRocm93IG5ldyBFcnJvcihcIlNpciwgdGhpcyBpcyBhIFdlbmR5J3NcIik7XG4gIH1cblxuICAvLyBpZiAoIUFMTE9XX09SSUdJTlMuaW5jbHVkZXMoZXZlbnQub3JpZ2luKSkge1xuICAvLyAgIHRocm93IG5ldyBFcnJvcignTWVzc2FnZSBvcmlnaW4gaXMgbm90IGluIHRoZSBhbGxvd2VkIGxpc3QnKTtcbiAgLy8gfVxuXG4gIGlmICh0eXBlb2YgZXZlbnQuZGF0YSAhPT0gJ29iamVjdCcgfHwgZXZlbnQuZGF0YS50eXBlICE9PSBNRVNTQUdFX1RZUEUpIHtcbiAgICB0aHJvdyBuZXcgRXJyb3IoYE1lc3NhZ2UgdHlwZSBkb2VzIG5vdCBtYXRjaCB0eXBlIHVzZWQgZm9yIGVtYmVkZGVkIGNvbW1zYCk7XG4gIH1cbn1cblxud2luZG93LmFkZEV2ZW50TGlzdGVuZXIoJ21lc3NhZ2UnLCBmdW5jdGlvbiAoZXZlbnQpIHtcbiAgdHJ5IHtcbiAgICB2YWxpZGF0ZU1lc3NhZ2VFdmVudChldmVudCk7XG4gIH0gY2F0Y2ggKGVycikge1xuICAgIGxvZygnaWdub3JpbmcgbWVzc2FnZScsIGVyciwgZXZlbnQpO1xuICAgIHJldHVybjtcbiAgfVxuXG4gIGNvbnN0IHBvcnQgPSBldmVudC5wb3J0cz8uWzBdO1xuICBpZiAoZXZlbnQuZGF0YS5oYW5kc2hha2UgPT09ICdwb3J0IHRyYW5zZmVyJyAmJiBwb3J0KSB7XG4gICAgbG9nKCdtZXNzYWdlIHBvcnQgcmVjZWl2ZWQnLCBldmVudCk7XG5cbiAgICBjb25zdCBzd2l0Y2hib2FyZCA9IG5ldyBTd2l0Y2hib2FyZCh7XG4gICAgICBwb3J0LFxuICAgICAgbmFtZTogJ3N1cGVyc2V0JyxcbiAgICAgIGRlYnVnOiBkZWJ1Z01vZGUsXG4gICAgfSk7XG5cbiAgICBzd2l0Y2hib2FyZC5kZWZpbmVNZXRob2QoJ2d1ZXN0VG9rZW4nLCAoeyBndWVzdFRva2VuIH0pID0+IHtcbiAgICAgIHN0YXJ0KGd1ZXN0VG9rZW4pO1xuICAgIH0pO1xuXG4gICAgc3dpdGNoYm9hcmQuZGVmaW5lTWV0aG9kKCdnZXRTY3JvbGxTaXplJywgKCkgPT4gKHtcbiAgICAgIHdpZHRoOiBkb2N1bWVudC5ib2R5LnNjcm9sbFdpZHRoLFxuICAgICAgaGVpZ2h0OiBkb2N1bWVudC5ib2R5LnNjcm9sbEhlaWdodCxcbiAgICB9KSk7XG5cbiAgICBzd2l0Y2hib2FyZC5zdGFydCgpO1xuICB9XG59KTtcblxubG9nKCdlbWJlZCBwYWdlIGlzIHJlYWR5IHRvIHJlY2VpdmUgbWVzc2FnZXMnKTtcbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///./src/embedded/index.tsx\n");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			id: moduleId,
/******/ 			loaded: false,
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = __webpack_modules__;
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/amd define */
/******/ 	(() => {
/******/ 		__webpack_require__.amdD = function () {
/******/ 			throw new Error('define cannot be used indirect');
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/amd options */
/******/ 	(() => {
/******/ 		__webpack_require__.amdO = {};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/chunk loaded */
/******/ 	(() => {
/******/ 		var deferred = [];
/******/ 		__webpack_require__.O = (result, chunkIds, fn, priority) => {
/******/ 			if(chunkIds) {
/******/ 				priority = priority || 0;
/******/ 				for(var i = deferred.length; i > 0 && deferred[i - 1][2] > priority; i--) deferred[i] = deferred[i - 1];
/******/ 				deferred[i] = [chunkIds, fn, priority];
/******/ 				return;
/******/ 			}
/******/ 			var notFulfilled = Infinity;
/******/ 			for (var i = 0; i < deferred.length; i++) {
/******/ 				var [chunkIds, fn, priority] = deferred[i];
/******/ 				var fulfilled = true;
/******/ 				for (var j = 0; j < chunkIds.length; j++) {
/******/ 					if ((priority & 1 === 0 || notFulfilled >= priority) && Object.keys(__webpack_require__.O).every((key) => (__webpack_require__.O[key](chunkIds[j])))) {
/******/ 						chunkIds.splice(j--, 1);
/******/ 					} else {
/******/ 						fulfilled = false;
/******/ 						if(priority < notFulfilled) notFulfilled = priority;
/******/ 					}
/******/ 				}
/******/ 				if(fulfilled) {
/******/ 					deferred.splice(i--, 1)
/******/ 					var r = fn();
/******/ 					if (r !== undefined) result = r;
/******/ 				}
/******/ 			}
/******/ 			return result;
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/chunk preload function */
/******/ 	(() => {
/******/ 		__webpack_require__.H = {};
/******/ 		__webpack_require__.G = (chunkId) => {
/******/ 			Object.keys(__webpack_require__.H).map((key) => {
/******/ 				__webpack_require__.H[key](chunkId);
/******/ 			});
/******/ 		}
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/compat get default export */
/******/ 	(() => {
/******/ 		// getDefaultExport function for compatibility with non-harmony modules
/******/ 		__webpack_require__.n = (module) => {
/******/ 			var getter = module && module.__esModule ?
/******/ 				() => (module['default']) :
/******/ 				() => (module);
/******/ 			__webpack_require__.d(getter, { a: getter });
/******/ 			return getter;
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/create fake namespace object */
/******/ 	(() => {
/******/ 		var getProto = Object.getPrototypeOf ? (obj) => (Object.getPrototypeOf(obj)) : (obj) => (obj.__proto__);
/******/ 		var leafPrototypes;
/******/ 		// create a fake namespace object
/******/ 		// mode & 1: value is a module id, require it
/******/ 		// mode & 2: merge all properties of value into the ns
/******/ 		// mode & 4: return value when already ns object
/******/ 		// mode & 16: return value when it's Promise-like
/******/ 		// mode & 8|1: behave like require
/******/ 		__webpack_require__.t = function(value, mode) {
/******/ 			if(mode & 1) value = this(value);
/******/ 			if(mode & 8) return value;
/******/ 			if(typeof value === 'object' && value) {
/******/ 				if((mode & 4) && value.__esModule) return value;
/******/ 				if((mode & 16) && typeof value.then === 'function') return value;
/******/ 			}
/******/ 			var ns = Object.create(null);
/******/ 			__webpack_require__.r(ns);
/******/ 			var def = {};
/******/ 			leafPrototypes = leafPrototypes || [null, getProto({}), getProto([]), getProto(getProto)];
/******/ 			for(var current = mode & 2 && value; typeof current == 'object' && !~leafPrototypes.indexOf(current); current = getProto(current)) {
/******/ 				Object.getOwnPropertyNames(current).forEach((key) => (def[key] = () => (value[key])));
/******/ 			}
/******/ 			def['default'] = () => (value);
/******/ 			__webpack_require__.d(ns, def);
/******/ 			return ns;
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/ensure chunk */
/******/ 	(() => {
/******/ 		__webpack_require__.f = {};
/******/ 		// This file contains only the entry chunk.
/******/ 		// The chunk loading function for additional chunks
/******/ 		__webpack_require__.e = (chunkId) => {
/******/ 			return Promise.all(Object.keys(__webpack_require__.f).reduce((promises, key) => {
/******/ 				__webpack_require__.f[key](chunkId, promises);
/******/ 				return promises;
/******/ 			}, []));
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/get javascript chunk filename */
/******/ 	(() => {
/******/ 		// This function allow to reference async chunks
/******/ 		__webpack_require__.u = (chunkId) => {
/******/ 			// return url for filenames not based on template
/******/ 			if (chunkId === "thumbnail") return "" + chunkId + ".f7bfae86.entry.js";
/******/ 			if (chunkId === "vendors-node_modules_d3-tip_index_js-node_modules_dompurify_dist_purify_js-node_modules_echar-a756c7") return "" + chunkId + ".72f0e548.entry.js";
/******/ 			if (chunkId === "src_setup_setupPlugins_ts") return "" + chunkId + ".444684fd.entry.js";
/******/ 			// return url for filenames based on template
/******/ 			return "" + chunkId + "." + {"node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_alert_svg":"b4a759fd","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_alert_solid_svg":"368a443c","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_alert_soli-636446":"f6637556","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_ballot_svg":"bc63e720","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_binoculars_svg":"8c9d9653","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_bolt_svg":"d399aacf","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_bolt_small_svg":"dd501e04","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_bolt_small-6d3f7b":"21379cc1","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_calendar_svg":"2891afec","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_cancel-x_svg":"8a67fcc3","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_cancel_svg":"322a72f1","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_cancel_solid_svg":"a661418e","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_card_view_svg":"fdbb7680","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_cards_svg":"3c35bf06","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_cards_locked_svg":"f20c45c9","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_caret_down_svg":"322fc92a","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_caret_left_svg":"67dc047a","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_caret_right_svg":"a617194c","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_caret_up_svg":"ef3a775b","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_category_svg":"f13824ab","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_certified_svg":"701cd33f","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_check_svg":"8df71afc","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_checkbox-h-aaa839":"7a229b6d","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_checkbox-off_svg":"8b04376b","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_checkbox-on_svg":"5ef0f651","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_circle_svg":"1eb6a81b","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_circle_check_svg":"22512ab6","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_circle_che-4a02ca":"b9ea9d0f","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_clock_svg":"ead937e1","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_close_svg":"4d4f8a2c","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_code_svg":"5c3f3013","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_cog_svg":"ab781eb0","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_collapse_svg":"e0b1306f","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_color_pale-2eeb8a":"c5d388c9","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_components_svg":"4527215d","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_copy_svg":"d212c2b3","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_cross-filt-701026":"3eec5d40","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_cursor_tar-715a18":"2b8c56d6","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_database_svg":"ba014064","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_dataset_ph-4dd5d0":"c4457d60","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_dataset_vi-67b24b":"1a61372e","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_dataset_vi-686dd1":"e1679902","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_default_db-f09645":"1629a015","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_download_svg":"1631aab7","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_drag_svg":"59100af3","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_edit_svg":"0557f942","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_edit_alt_svg":"bd070673","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_email_svg":"ed410277","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_error_svg":"93287d78","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_error_solid_svg":"79b8632d","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_error_soli-75fe06":"8bbf3fe5","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_error_soli-b8c300":"d83a2b6a","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_exclamation_svg":"767b5328","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_expand_svg":"9108a403","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_eye_svg":"a0a8bcad","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_eye_slash_svg":"3632e874","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_favorite-s-0022ac":"1f662e8f","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_favorite-u-065d30":"feb590f7","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_favorite_s-6d3f4f":"44396f36","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_field_abc_svg":"2e87c3f5","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_field_bool-c3e3ab":"4e40a895","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_field_date_svg":"d5b0e432","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_field_deri-0477fc":"426bef26","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_field_num_svg":"75a8a2f2","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_field_struct_svg":"18158800","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_file_svg":"36dd3d14","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_filter_svg":"cc0b68ed","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_filter_small_svg":"98e70c18","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_folder_svg":"c64fe96a","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_full_svg":"6836a078","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_function_x_svg":"67f52efc","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_gear_svg":"ca95d286","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_grid_svg":"0b9d89fa","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_image_svg":"0fe055bd","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_import_svg":"a5fbf465","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_info-solid_svg":"3a5a4957","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_info_svg":"c49b9651","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_info_solid-774f41":"aa07fa24","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_join_svg":"75118617","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_keyboard_svg":"9b25947f","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_layers_svg":"e3c236ed","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_lightbulb_svg":"f88c79f5","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_link_svg":"a9c9a539","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_list_svg":"41455e41","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_list_view_svg":"6b9ab191","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_location_svg":"a7a3d378","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_lock_locked_svg":"e290a3cd","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_lock_unloc-d05a82":"277b419c","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_map_svg":"9ff743b9","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_message_svg":"ae651d43","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_minus_svg":"0c09d4cd","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_minus_solid_svg":"3617cfde","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_more_horiz_svg":"152096a9","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_more_vert_svg":"f98f5c3b","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_move_svg":"0d67d241","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_nav_charts_svg":"c5cec6a1","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_nav_dashbo-57e6a8":"61c221e7","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_nav_data_svg":"f062410b","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_nav_explore_svg":"ea614362","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_nav_home_svg":"aacf1d79","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_nav_lab_svg":"67d60772","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_note_svg":"7b5eb9e9","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_offline_svg":"1a21d7b6","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_paperclip_svg":"2bff9705","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_placeholder_svg":"e4be109f","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_plus_svg":"e69ee8b9","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_plus_large_svg":"7f50cf85","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_plus_small_svg":"d68d7d69","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_plus_solid_svg":"551f6b58","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_queued_svg":"c33fc857","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_refresh_svg":"8c98657a","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_running_svg":"6df9102f","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_save_svg":"5a90e9d1","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_search_svg":"4eb1763d","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_server_svg":"6199f1f8","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_share_svg":"2142568a","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_slack_svg":"e48e277d","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_sort_svg":"77afceb0","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_sort_asc_svg":"6c4a5e16","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_sort_desc_svg":"51d32617","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_sql_svg":"02052c96","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_table_svg":"ee62f065","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_tag_svg":"223aa6f9","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_tags_svg":"5ef0023d","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_transparent_svg":"9e0d065d","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_trash_svg":"0df8f570","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_triangle_c-25b7e8":"8798f9ea","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_triangle_d-e062ce":"af369a00","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_triangle_up_svg":"317da97d","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_up-level_svg":"6b725144","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_user_svg":"12a7230d","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_warning_svg":"d38332bf","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_warning_so-57941a":"9ae48824","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_x-large_svg":"052916a0","node_modules_svgr_webpack_lib_index_js_-svgo_titleProp_ref_src_assets_images_icons_x-small_svg":"fd5d5b23","src_explore_components_controls_AnnotationLayerControl_AnnotationLayer_jsx":"b45d9abd","src_components_Datasource_DatasourceEditor_jsx":"42b6c3cc","node_modules_brace_mode_sql_js":"45718780","node_modules_brace_mode_markdown_js":"e9aa615c","node_modules_brace_mode_css_js":"19380be8","node_modules_brace_mode_json_js":"40149365","node_modules_brace_mode_yaml_js":"034104b9","node_modules_brace_mode_html_js":"eb5cdec4","node_modules_brace_mode_javascript_js":"6c85cd7e","node_modules_brace_theme_textmate_js":"d8fe6574","node_modules_brace_theme_github_js":"5ee163de","node_modules_brace_ext_language_tools_js":"bc6bc53a","node_modules_brace_index_js":"f641c003","node_modules_react-ace_lib_index_js":"2ec0871c","node_modules_lodash_lodash_js":"f911c9da","packages_superset-ui-chart-controls_src_index_ts":"3c093299","packages_superset-ui-core_src_index_ts":"8e964efe","DashboardPage":"9706041b","vendors-node_modules_react-map-gl_dist_esm_index_js-node_modules_mapbox-gl_dist_mapbox-gl_css":"3a3d4ac4","plugins_legacy-preset-chart-deckgl_src_layers_Arc_Arc_jsx-data_image_svg_xml_charset_utf-8_3C-6e01b4":"23c11d1e","plugins_legacy-preset-chart-deckgl_src_layers_Geojson_Geojson_jsx-data_image_svg_xml_charset_-fcbc94":"bba92f45","vendors-node_modules_deck_gl_aggregation-layers_dist_esm_aggregation-layer_js-node_modules_de-7aa3e6":"9915c610","plugins_legacy-preset-chart-deckgl_src_layers_Grid_Grid_jsx-data_image_svg_xml_charset_utf-8_-32e007":"a78a0f3a","plugins_legacy-preset-chart-deckgl_src_layers_Hex_Hex_jsx-data_image_svg_xml_charset_utf-8_3C-f18b07":"92ab0b48","plugins_legacy-preset-chart-deckgl_src_Multi_Multi_jsx-data_image_svg_xml_charset_utf-8_3C_xm-efe338":"07abf270","plugins_legacy-preset-chart-deckgl_src_layers_Path_Path_jsx-data_image_svg_xml_charset_utf-8_-1f71a6":"ff1c9521","plugins_legacy-preset-chart-deckgl_src_layers_Polygon_Polygon_jsx-data_image_svg_xml_charset_-3495ae":"5a7d5686","plugins_legacy-preset-chart-deckgl_src_layers_Scatter_Scatter_jsx-data_image_svg_xml_charset_-8cb8ed":"2b418a40","plugins_legacy-preset-chart-deckgl_src_layers_Screengrid_Screengrid_jsx-data_image_svg_xml_ch-28f53c":"b0a3aec0","src_filters_components_Select_SelectFilterPlugin_tsx":"c943dd5b","src_filters_components_Range_RangeFilterPlugin_tsx":"3dd005ba","node_modules_rc-picker_es_generate_moment_js-node_modules_rc-picker_es_index_js-src_filters_c-2f4e13":"84fe8bfb","src_filters_components_TimeColumn_TimeColumnFilterPlugin_tsx":"cc180282","src_filters_components_GroupBy_GroupByFilterPlugin_tsx":"91d19524","src_filters_components_TimeGrain_TimeGrainFilterPlugin_tsx":"05c6d829","node_modules_array-move_index_js-node_modules_css-loader_dist_runtime_api_js-node_modules_css-b5847c":"c890ab7f","src_visualizations_TimeTable_TimeTable_jsx":"9b116172","plugins_legacy-preset-chart-nvd3_src_ReactNVD3_jsx":"587aa8a1","plugins_plugin-chart-echarts_src_BigNumber_BigNumberViz_tsx":"592a82ce","plugins_plugin-chart-echarts_src_BoxPlot_EchartsBoxPlot_tsx":"0973be30","plugins_legacy-plugin-chart-calendar_src_ReactCalendar_jsx":"01be190a","plugins_legacy-plugin-chart-chord_src_ReactChord_jsx":"c591a273","plugins_legacy-plugin-chart-country-map_src_ReactCountryMap_js":"7c7247cc","vendors-node_modules_data-ui_event-flow_build_index_js":"7d405a18","plugins_legacy-plugin-chart-event-flow_src_EventFlow_tsx":"1240dd3a","plugins_legacy-plugin-chart-event-flow_src_transformProps_ts":"c71848d3","plugins_plugin-chart-echarts_src_Funnel_EchartsFunnel_tsx":"4e9a7b94","plugins_plugin-chart-echarts_src_Treemap_EchartsTreemap_tsx":"f13cfdca","plugins_plugin-chart-echarts_src_Gauge_EchartsGauge_tsx":"8e82591c","plugins_plugin-chart-echarts_src_Graph_EchartsGraph_tsx":"55f3b4c7","plugins_plugin-chart-echarts_src_Radar_EchartsRadar_tsx":"5079c93f","plugins_plugin-chart-echarts_src_MixedTimeseries_EchartsMixedTimeseries_tsx":"d94f52fb","plugins_legacy-plugin-chart-heatmap_src_ReactHeatmap_js":"4a3ac251","plugins_legacy-plugin-chart-histogram_src_Histogram_jsx":"8a6994a5","plugins_legacy-plugin-chart-horizon_src_HorizonChart_jsx":"b33555ba","plugins_legacy-plugin-chart-map-box_src_MapBox_jsx-data_image_svg_xml_charset_utf-8_3C_xml_ve-d1d060":"a588e17b","plugins_legacy-plugin-chart-map-box_src_transformProps_js-data_image_svg_xml_charset_utf-8_3C-7bff5d":"569588e8","plugins_legacy-plugin-chart-paired-t-test_src_PairedTTest_jsx":"f789a8a9","plugins_legacy-plugin-chart-parallel-coordinates_src_ReactParallelCoordinates_jsx":"8a1c53b0","plugins_legacy-plugin-chart-partition_src_ReactPartition_js":"adf17d0b","plugins_plugin-chart-echarts_src_Pie_EchartsPie_tsx":"b66b2938","plugins_legacy-plugin-chart-pivot-table_src_ReactPivotTable_js":"24f51e4a","plugins_plugin-chart-pivot-table_src_PivotTableChart_tsx":"8eda5e4b","plugins_legacy-plugin-chart-rose_src_ReactRose_js":"42128c61","plugins_legacy-plugin-chart-sankey_src_ReactSankey_jsx":"f6c5f979","plugins_legacy-plugin-chart-sunburst_src_ReactSunburst_js":"a4a14a0b","plugins_plugin-chart-table_src_TableChart_tsx":"332e6a5b","plugins_legacy-plugin-chart-treemap_src_ReactTreemap_js":"e8f6fac8","plugins_plugin-chart-word-cloud_src_chart_WordCloud_tsx":"874dd871","plugins_legacy-plugin-chart-world-map_src_ReactWorldMap_jsx":"c9737711","plugins_plugin-chart-echarts_src_Timeseries_EchartsTimeseries_tsx":"75cb8cb0","plugins_plugin-chart-echarts_src_Tree_EchartsTree_tsx":"b731056d","DashboardContainer":"ffc4b717"}[chunkId] + ".chunk.js";
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/getFullHash */
/******/ 	(() => {
/******/ 		__webpack_require__.h = () => ("f7d60efee9ba15f565a3")
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/global */
/******/ 	(() => {
/******/ 		__webpack_require__.g = (function() {
/******/ 			if (typeof globalThis === 'object') return globalThis;
/******/ 			try {
/******/ 				return this || new Function('return this')();
/******/ 			} catch (e) {
/******/ 				if (typeof window === 'object') return window;
/******/ 			}
/******/ 		})();
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/harmony module decorator */
/******/ 	(() => {
/******/ 		__webpack_require__.hmd = (module) => {
/******/ 			module = Object.create(module);
/******/ 			if (!module.children) module.children = [];
/******/ 			Object.defineProperty(module, 'exports', {
/******/ 				enumerable: true,
/******/ 				set: () => {
/******/ 					throw new Error('ES Modules may not assign module.exports or exports.*, Use ESM export syntax, instead: ' + module.id);
/******/ 				}
/******/ 			});
/******/ 			return module;
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/load script */
/******/ 	(() => {
/******/ 		var inProgress = {};
/******/ 		var dataWebpackPrefix = "superset:";
/******/ 		// loadScript function to load a script via script tag
/******/ 		__webpack_require__.l = (url, done, key, chunkId) => {
/******/ 			if(inProgress[url]) { inProgress[url].push(done); return; }
/******/ 			var script, needAttach;
/******/ 			if(key !== undefined) {
/******/ 				var scripts = document.getElementsByTagName("script");
/******/ 				for(var i = 0; i < scripts.length; i++) {
/******/ 					var s = scripts[i];
/******/ 					if(s.getAttribute("src") == url || s.getAttribute("data-webpack") == dataWebpackPrefix + key) { script = s; break; }
/******/ 				}
/******/ 			}
/******/ 			if(!script) {
/******/ 				needAttach = true;
/******/ 				script = document.createElement('script');
/******/ 		
/******/ 				script.charset = 'utf-8';
/******/ 				script.timeout = 120;
/******/ 				if (__webpack_require__.nc) {
/******/ 					script.setAttribute("nonce", __webpack_require__.nc);
/******/ 				}
/******/ 				script.setAttribute("data-webpack", dataWebpackPrefix + key);
/******/ 				script.src = url;
/******/ 			}
/******/ 			inProgress[url] = [done];
/******/ 			var onScriptComplete = (prev, event) => {
/******/ 				// avoid mem leaks in IE.
/******/ 				script.onerror = script.onload = null;
/******/ 				clearTimeout(timeout);
/******/ 				var doneFns = inProgress[url];
/******/ 				delete inProgress[url];
/******/ 				script.parentNode && script.parentNode.removeChild(script);
/******/ 				doneFns && doneFns.forEach((fn) => (fn(event)));
/******/ 				if(prev) return prev(event);
/******/ 			}
/******/ 			;
/******/ 			var timeout = setTimeout(onScriptComplete.bind(null, undefined, { type: 'timeout', target: script }), 120000);
/******/ 			script.onerror = onScriptComplete.bind(null, script.onerror);
/******/ 			script.onload = onScriptComplete.bind(null, script.onload);
/******/ 			needAttach && document.head.appendChild(script);
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/node module decorator */
/******/ 	(() => {
/******/ 		__webpack_require__.nmd = (module) => {
/******/ 			module.paths = [];
/******/ 			if (!module.children) module.children = [];
/******/ 			return module;
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/publicPath */
/******/ 	(() => {
/******/ 		__webpack_require__.p = "/static/assets/";
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/jsonp chunk loading */
/******/ 	(() => {
/******/ 		__webpack_require__.b = document.baseURI || self.location.href;
/******/ 		
/******/ 		// object to store loaded and loading chunks
/******/ 		// undefined = chunk not loaded, null = chunk preloaded/prefetched
/******/ 		// [resolve, reject, Promise] = chunk loading, 0 = chunk loaded
/******/ 		var installedChunks = {
/******/ 			"embedded": 0
/******/ 		};
/******/ 		
/******/ 		__webpack_require__.f.j = (chunkId, promises) => {
/******/ 				// JSONP chunk loading for javascript
/******/ 				var installedChunkData = __webpack_require__.o(installedChunks, chunkId) ? installedChunks[chunkId] : undefined;
/******/ 				if(installedChunkData !== 0) { // 0 means "already installed".
/******/ 		
/******/ 					// a Promise means "currently loading".
/******/ 					if(installedChunkData) {
/******/ 						promises.push(installedChunkData[2]);
/******/ 					} else {
/******/ 						if(true) { // all chunks have JS
/******/ 							// setup Promise in chunk cache
/******/ 							var promise = new Promise((resolve, reject) => (installedChunkData = installedChunks[chunkId] = [resolve, reject]));
/******/ 							promises.push(installedChunkData[2] = promise);
/******/ 		
/******/ 							// start chunk loading
/******/ 							var url = __webpack_require__.p + __webpack_require__.u(chunkId);
/******/ 							// create error before stack unwound to get useful stacktrace later
/******/ 							var error = new Error();
/******/ 							var loadingEnded = (event) => {
/******/ 								if(__webpack_require__.o(installedChunks, chunkId)) {
/******/ 									installedChunkData = installedChunks[chunkId];
/******/ 									if(installedChunkData !== 0) installedChunks[chunkId] = undefined;
/******/ 									if(installedChunkData) {
/******/ 										var errorType = event && (event.type === 'load' ? 'missing' : event.type);
/******/ 										var realSrc = event && event.target && event.target.src;
/******/ 										error.message = 'Loading chunk ' + chunkId + ' failed.\n(' + errorType + ': ' + realSrc + ')';
/******/ 										error.name = 'ChunkLoadError';
/******/ 										error.type = errorType;
/******/ 										error.request = realSrc;
/******/ 										installedChunkData[1](error);
/******/ 									}
/******/ 								}
/******/ 							};
/******/ 							__webpack_require__.l(url, loadingEnded, "chunk-" + chunkId, chunkId);
/******/ 						} else installedChunks[chunkId] = 0;
/******/ 					}
/******/ 				}
/******/ 		};
/******/ 		
/******/ 		// no prefetching
/******/ 		
/******/ 		__webpack_require__.H.j = (chunkId) => {
/******/ 			if((!__webpack_require__.o(installedChunks, chunkId) || installedChunks[chunkId] === undefined) && true) {
/******/ 				installedChunks[chunkId] = null;
/******/ 				var link = document.createElement('link');
/******/ 		
/******/ 				link.charset = 'utf-8';
/******/ 				if (__webpack_require__.nc) {
/******/ 					link.setAttribute("nonce", __webpack_require__.nc);
/******/ 				}
/******/ 				link.rel = "preload";
/******/ 				link.as = "script";
/******/ 				link.href = __webpack_require__.p + __webpack_require__.u(chunkId);
/******/ 				document.head.appendChild(link);
/******/ 			}
/******/ 		};
/******/ 		
/******/ 		// no HMR
/******/ 		
/******/ 		// no HMR manifest
/******/ 		
/******/ 		__webpack_require__.O.j = (chunkId) => (installedChunks[chunkId] === 0);
/******/ 		
/******/ 		// install a JSONP callback for chunk loading
/******/ 		var webpackJsonpCallback = (parentChunkLoadingFunction, data) => {
/******/ 			var [chunkIds, moreModules, runtime] = data;
/******/ 			// add "moreModules" to the modules object,
/******/ 			// then flag all "chunkIds" as loaded and fire callback
/******/ 			var moduleId, chunkId, i = 0;
/******/ 			if(chunkIds.some((id) => (installedChunks[id] !== 0))) {
/******/ 				for(moduleId in moreModules) {
/******/ 					if(__webpack_require__.o(moreModules, moduleId)) {
/******/ 						__webpack_require__.m[moduleId] = moreModules[moduleId];
/******/ 					}
/******/ 				}
/******/ 				if(runtime) var result = runtime(__webpack_require__);
/******/ 			}
/******/ 			if(parentChunkLoadingFunction) parentChunkLoadingFunction(data);
/******/ 			for(;i < chunkIds.length; i++) {
/******/ 				chunkId = chunkIds[i];
/******/ 				if(__webpack_require__.o(installedChunks, chunkId) && installedChunks[chunkId]) {
/******/ 					installedChunks[chunkId][0]();
/******/ 				}
/******/ 				installedChunks[chunkIds[i]] = 0;
/******/ 			}
/******/ 			return __webpack_require__.O(result);
/******/ 		}
/******/ 		
/******/ 		var chunkLoadingGlobal = globalThis["webpackChunksuperset"] = globalThis["webpackChunksuperset"] || [];
/******/ 		chunkLoadingGlobal.forEach(webpackJsonpCallback.bind(null, 0));
/******/ 		chunkLoadingGlobal.push = webpackJsonpCallback.bind(null, chunkLoadingGlobal.push.bind(chunkLoadingGlobal));
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/chunk preload trigger */
/******/ 	(() => {
/******/ 		var chunkToChildrenMap = {
/******/ 			"DashboardPage": [
/******/ 				"vendors",
/******/ 				"DashboardContainer"
/******/ 			]
/******/ 		};
/******/ 		__webpack_require__.f.preload = (chunkId) => {
/******/ 			var chunks = chunkToChildrenMap[chunkId];
/******/ 			Array.isArray(chunks) && chunks.map(__webpack_require__.G);
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
/******/ 	
/******/ 	// module factories are used so entry inlining is disabled
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	__webpack_require__.O(undefined, ["vendors","vendors-node_modules_ctrl_tinycolor_dist_module_index_js-node_modules_ansi-html-community_ind-be20b6","vendors-node_modules_react-icons_all-files_fa_FaAlignCenter_js-node_modules_react-icons_all-f-e932c6","src_dashboard_actions_hydrate_js","src_modules_utils_js-node_modules_moment_locale_sync_recursive_-node_modules_react-router-dom-fd68f1"], () => (__webpack_require__("./node_modules/webpack-dev-server/client/index.js?http://localhost:9000")))
/******/ 	__webpack_require__.O(undefined, ["vendors","vendors-node_modules_ctrl_tinycolor_dist_module_index_js-node_modules_ansi-html-community_ind-be20b6","vendors-node_modules_react-icons_all-files_fa_FaAlignCenter_js-node_modules_react-icons_all-f-e932c6","src_dashboard_actions_hydrate_js","src_modules_utils_js-node_modules_moment_locale_sync_recursive_-node_modules_react-router-dom-fd68f1"], () => (__webpack_require__("./src/preamble.ts")))
/******/ 	var __webpack_exports__ = __webpack_require__.O(undefined, ["vendors","vendors-node_modules_ctrl_tinycolor_dist_module_index_js-node_modules_ansi-html-community_ind-be20b6","vendors-node_modules_react-icons_all-files_fa_FaAlignCenter_js-node_modules_react-icons_all-f-e932c6","src_dashboard_actions_hydrate_js","src_modules_utils_js-node_modules_moment_locale_sync_recursive_-node_modules_react-router-dom-fd68f1"], () => (__webpack_require__("./src/embedded/index.tsx")))
/******/ 	__webpack_exports__ = __webpack_require__.O(__webpack_exports__);
/******/ 	
/******/ })()
;