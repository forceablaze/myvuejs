export default [
  { text:"CLV_OCP_INITIALIZE", value: 0 },
  { text:"CLV_OCP_OPEN", value: 1 },
  { text:"CLV_TC_SETTING", value: 2 },
  { text:"CLV_START_COMMUNICATION", value: 3 },
  { text:"CLV_STOP_COMMUNICATION", value: 4 },
  { text:"CLV_OCP_CHANGE_DEVICE", value: 5 },
  { text:"UCES_OCP_INITIALIZE", value: 6 },
  { text:"UCES_OCP_OPEN", value: 7 },
  { text:"UCES_TC_SETTING", value: 8 },
  { text:"UCES_START_COMMUNICATION", value: 9 },
  { text:"DATA_MAX", value: 10 },
  { text:"EXECUTE_START", value: 11 },
  { text:"EXECUTE_END", value: 12 },
  { text:"STATE_NOTIFY", value: 13 },
  { text:"INSTRUCT", value: 14 },
  { text:"PRM_LOAD", value: 15 },
  { text:"PRM_SAVE", value: 16 },
  { text:"Reserve", value: 17 },
  { text:"WRITE_PERSISTENT_DATA", value: 18 },
  { text:"READ_PERSISTENT_DATA", value: 19 },
  { text:"WRITE_INDIVISUAL_DATA", value: 20 },
  { text:"READ_INDIVISUAL_DATA", value: 21 },
  { text:"DDR_CAPTURE", value: 22 },
  { text:"GET_MEMAREA", value: 23 },
  { text:"SET_INPUT_FORMAT", value: 24 },
  { text:"SET_OUTPUT_FORMAT", value: 25 },
  { text:"CONTROL_MEMAREA", value: 26 },
  { text:"MEMORY_TEST", value: 27 },
  { text:"SET_NO_TRANSFER_IMAGE_REMOVE_MODE", value: 28 },
  { text:"CTRL_MEDIA_LED_BLINK", value: 29 },
  { text:"BLINK_MEDIA_LED_ABSOLUTELY", value: 30 },
  { text:"DATA_BACKUP", value: 31 },
  { text:"DATA_RESTORE", value: 32 },
  { text:"DATA_LIST_OPEN", value: 33 },
  { text:"DATA_LIST_CTRL_GET_COUNT", value: 34 },
  { text:"DATA_LIST_CTRL_GET_INFO", value: 35 },
  { text:"DATA_LIST_CLOSE", value: 36 },
  { text:"DATA_DELETE", value: 37 },
  { text:"DATA_RESTORE_FINISH", value: 38 },
  { text:"SCOPEID_DATA_SAVE", value: 39 },
  { text:"SCOPEID_DATA_LOAD", value: 40 },
  { text:"SCOPEID_DATA_LIST_OPEN", value: 41 },
  { text:"SCOPEID_DATA_LIST_CTRL_GET_COUNT", value: 42 },
  { text:"SCOPEID_DATA_LIST_CTRL_GET_INFO", value: 43 },
  { text:"SCOPEID_DATA_LIST_CLOSE", value: 44 },
  { text:"SCOPEID_DATA_DELETE", value: 45 },
  { text:"SETTING_SAVE", value: 46 },
  { text:"SETTING_LOAD", value: 47 },
  { text:"ALL_SETTINGS_LIST_OPEN", value: 48 },
  { text:"ALL_SETTINGS_LIST_CTRL_GET_COUNT", value: 49 },
  { text:"ALL_SETTINGS_LIST_CTRL_GET_INFO", value: 50 },
  { text:"ALL_SETTINGS_LIST_CLOSE", value: 51 },
  { text:"SETTING_DELETE", value: 52 },
  { text:"SETTING_LIST_OPEN", value: 53 },
  { text:"SETTING_LIST_CTRL_GET_COUNT", value: 54 },
  { text:"SETTING_LIST_CTRL_GET_INFO", value: 55 },
  { text:"SETTING_LIST_CLOSE", value: 56 },
  { text:"UPDATE_DATA_LIST_OPEN", value: 57 },
  { text:"UPDATE_DATA_LIST_CTRL_GET_PACKAGE", value: 58 },
  { text:"UPDATE_DATA_LIST_CTRL_GET_COUNT", value: 59 },
  { text:"UPDATE_DATA_LIST_CTRL_GET_INFO", value: 60 },
  { text:"UPDATE_DATA_LIST_CLOSE", value: 61 },
  { text:"GET_PREPARE_DATA", value: 62 },
  { text:"PREPARE_UPDATE_DATA", value: 63 },
  { text:"CLEANUP_UPDATE_DATA", value: 64 },
  { text:"RAWIMAGE_LIST_OPEN", value: 65 },
  { text:"RAWIMAGE_LIST_CTRL_GET_COUNT", value: 66 },
  { text:"RAWIMAGE_LIST_CTRL_GET_INFO", value: 67 },
  { text:"RAWIMAGE_LIST_CLOSE", value: 68 },
  { text:"NET_PROCEDURE_SAVE", value: 69 },
  { text:"NET_PROCEDURE_LOAD", value: 70 },
  { text:"NET_PROCEDURE_DELETE", value: 71 },
  { text:"NET_MWM_SAVE_ASYNC", value: 72 },
  { text:"NET_MWM_LIST_OPEN", value: 73 },
  { text:"NET_MWM_LIST_GET_COUNT", value: 74 },
  { text:"NET_MWM_LIST_GET_INFO", value: 75 },
  { text:"NET_MWM_LIST_CLOSE", value: 76 },
  { text:"NET_MWM_DELETE", value: 77 },
  { text:"NET_MWM_LIST_GET_INFO_ASYNC", value: 78 },
  { text:"FIO_OPEN", value: 79 },
  { text:"FIO_CLOSE", value: 80 },
  { text:"FIO_READ", value: 81 },
  { text:"FIO_WRITE", value: 82 },
  { text:"FIO_CLOSE_WITH_CANCEL_INFO", value: 83 },
  { text:"CHECK_EXTERNAL_MEM_ENC_PW", value: 84 },
  { text:"TLS_CERTIFICATION_IMPORT", value: 85 },
  { text:"TLS_CERTIFICATION_DELETE", value: 86 },
  { text:"COPY_CP_FILE_TO_NET", value: 87 },
  { text:"TLS_CERTIFICATION_CHECK", value: 88 },
  { text:"EnableAutoDeleteTransferredFile", value: 89 },
  { text:"DisableAutoDeleteTransferredFile", value: 90 },
  { text:"ASYNC", value: 91 },
  { text:"GetLogAmount", value: 92 },
  { text:"WriteLogData", value: 93 },
  { text:"Transfer", value: 94 },
  { text:"ReadLogFileOpen", value: 95 },
  { text:"ReadLogFileGetInfo", value: 96 },
  { text:"ReadLogFileGetData", value: 97 },
  { text:"ReadLogFileClose", value: 98 },
  { text:"ReadLogFileSetPosition", value: 99 },
  { text:"ClearLogData", value: 100 },
  { text:"ReadLogFileGetDataCount", value: 101 },
  { text:"SetBodyId", value: 102 },
  { text:"ReadLogFileForServerOpen", value: 103 },
  { text:"ReadLogFileGetDataAsync", value: 104 },
  { text:"UpdateLogState", value: 105 },
  { text:"FORMAT", value: 106 },
  { text:"EXAM_CREATE", value: 107 },
  { text:"EXAM_OPEN", value: 108 },
  { text:"EXAM_CLOSE", value: 109 },
  { text:"EXAM_StudyInstanceUid2ExamId", value: 110 },
  { text:"EXAM_GetExamHistory", value: 111 },
  { text:"MEDIA_FORMAT", value: 112 },
  { text:"MEDIA_DISABLE", value: 113 },
  { text:"CREATE_PARTITION", value: 114 },
  { text:"GET_STORAGE_INFO", value: 115 },
  { text:"GET_SIZE_FOR_INITIALIZE_DB", value: 116 },
  { text:"READ_EXAMDB", value: 117 },
  { text:"CursorOpenFolderList", value: 118 },
  { text:"CursorOpenFileList", value: 119 },
  { text:"CursorClose", value: 120 },
  { text:"CursorGetCount", value: 121 },
  { text:"CursorGetInfo", value: 122 },
  { text:"GetExamFileName", value: 123 },
  { text:"DeleteRawImage", value: 124 },
  { text:"DeleteExamFolder", value: 125 },
  { text:"DeleteExamFile", value: 126 },
  { text:"DeleteResidualFile", value: 127 },
  { text:"EnableAutoDelete", value: 128 },
  { text:"DisableAutoDelete", value: 129 },
  { text:"CursorReset", value: 130 },
  { text:"GetFolderInfo", value: 131 },
  { text:"DeleteExamFileNoTrans", value: 132 },
  { text:"WriteLockMedia", value: 133 },
  { text:"WriteUnlockMedia", value: 134 },
  { text:"StartDeleteExamFile", value: 135 },
  { text:"EndDeleteExamFile", value: 136 },
  { text:"GetFolderInfoAsync", value: 137 },
  { text:"WriteLockMediaForUpdate", value: 138 },
  { text:"DeleteExamFileSync", value: 139 },
  { text:"OpenFolderSearch", value: 140 },
  { text:"OpenFolderSearchCancel", value: 141 },
  { text:"FreePhySpace", value: 142 },
  { text:"RecStart", value: 143 },
  { text:"RecStop", value: 144 },
  { text:"GetRecParam", value: 145 },
  { text:"GetRecInfo", value: 146 },
  { text:"PreviewStart", value: 147 },
  { text:"PreviewStop", value: 148 },
  { text:"DB_RecordPhotoInfo_forCapture", value: 149 },
  { text:"DB_DeletePhotoInfo_forCapture", value: 150 },
  { text:"DB_OpenTransferTarget", value: 151 },
  { text:"DB_UpdateTransferState", value: 152 },
  { text:"Storage_WriteFile", value: 153 },
  { text:"Storage_ReadFile", value: 154 },
  { text:"Storage_CopyFile", value: 155 },
  { text:"DB_GetExamInfo", value: 156 },
  { text:"GetExamFileName_Media", value: 157 },
  { text:"FileAddReserve", value: 158 },
  { text:"FileAddFix", value: 159 },
  { text:"FileAddCancel", value: 160 },
  { text:"DeleteRawBeforeRecord", value: 161 },
  { text:"RecordStillWaitExam", value: 162 },
  { text:"DB_MakeReadyTransfer", value: 163 },
  { text:"GET_STORAGE_INFO_DRIVERS", value: 164 },
  { text:"DB_OpenMedia", value: 165 },
  { text:"DB_CloseMedia", value: 166 },
  { text:"Storage_Pause", value: 167 },
  { text:"Storage_Restart", value: 168 },
  { text:"GetEntrySizeOfGetInfo", value: 169 },
  { text:"DB_GetImageInfo", value: 170 },
  { text:"DB_CleanUpTransfer", value: 171 },
  { text:"DB_GetAggregateInfo", value: 172 },
  { text:"MOV_RECOVER_FILE", value: 173 },
  { text:"MOV_RECOVER_INFO", value: 174 },
  { text:"DB_UpdateTransferStateExam", value: 175 },
  { text:"DB_UpdateTransferStateFile", value: 176 },
  { text:"GET_STORAGE_INFO_INTERNAL", value: 177 },
  { text:"UpdatePCFile", value: 178 },
  { text:"DB_TransferExam", value: 179 },
  { text:"FileAddReserve_v2", value: 180 },
  { text:"FileAddFix_v2", value: 181 },
  { text:"FileAddCancel_v2", value: 182 },
  { text:"FileAddReserveMov", value: 183 },
  { text:"FileAddFixMov", value: 184 },
  { text:"FileAddCancelMov", value: 185 },
  { text:"FileUpdateMov", value: 186 },
  { text:"DB_GetMovieRecordMedia", value: 187 },
  { text:"DB_ClearMovieInfo", value: 188 },
  { text:"DB_BackupMovieData", value: 189 },
  { text:"DB_DeleteReserveMovieData", value: 190 },
  { text:"DB_GetRecInfo", value: 191 },
  { text:"DB_RecordingMovieInfo", value: 192 },
  { text:"GetFolderSearchProgress", value: 193 },
  { text:"PreOpenFolderSearch", value: 194 },
  { text:"DB_GetSubRecordState", value: 195 },
  { text:"DB_GetFreeSpaceForJournal", value: 196 },
  { text:"FileAddReserveRaw", value: 197 },
  { text:"FileAddFixRaw", value: 198 },
  { text:"FileAddCancelRaw", value: 199 },
  { text:"DB_GetDBFileSize", value: 200 },
  { text:"READ_EXAMDB", value: 201 },
  { text:"Transfer", value: 202 },
  { text:"GetFileList", value: 203 },
  { text:"UpdateState", value: 204 },
  { text:"FileCtrl", value: 205 },
  { text:"FileRead", value: 206 },
  { text:"FileWrite", value: 207 },
  { text:"GetFileListByFile", value: 208 },
  { text:"APP", value: 209 },
  { text:"GUI", value: 210 },
  { text:"Reserve", value: 211 },
  { text:"LampMonitor", value: 212 },
  { text:"Lamp", value: 213 },
  { text:"GetLampState", value: 214 },
  { text:"ChangeObservationMode", value: 215 },
  { text:"GetObservationMode", value: 216 },
  { text:"LightGuideMonitor", value: 217 },
  { text:"GetLightGuideState", value: 218 },
  { text:"SetIntensity", value: 219 },
  { text:"SetBrightnessLevel", value: 220 },
  { text:"SetBrightnessMode", value: 221 },
  { text:"SetScopeTypeData", value: 222 },
  { text:"SetScopeIDData", value: 223 },
  { text:"SetIrisSpeed", value: 224 },
  { text:"SetBrightnessTarget", value: 225 },
  { text:"ErrorMonitor", value: 226 },
  { text:"GetError", value: 227 },
  { text:"GetTemperature", value: 228 },
  { text:"GetFanControl", value: 229 },
  { text:"SetSystemMode", value: 230 },
  { text:"SetMode", value: 231 },
  { text:"SetCalibration", value: 232 },
  { text:"BrightnessControl", value: 233 },
  { text:"AirPump", value: 234 },
  { text:"SetAirPumpPressure", value: 235 },
  { text:"SetExposureInfo", value: 236 },
  { text:"SetBrightnessSignal", value: 237 },
  { text:"SetPreLightMaintenance", value: 238 },
  { text:"SetAnalogScopeState", value: 239 },
  { text:"GetCurrent", value: 240 },
  { text:"GetPwmDuty", value: 241 },
  { text:"AutoLightLimitingMonitor", value: 242 },
  { text:"GetLightLimitingState", value: 243 },
  { text:"GetLightCorrectParam", value: 244 },
  { text:"GetLightSourceSpectrum", value: 245 },
  { text:"SetScopeState", value: 246 },
  { text:"SetSyncSignalInput", value: 247 },
  { text:"SetAnalogScopeTypeData", value: 248 },
  { text:"GetColorToneExtCv", value: 249 },
  { text:"Freeze", value: 250 },
  { text:"SetEnhance", value: 251 },
  { text:"SetEnhance_F", value: 252 },
  { text:"SetBrightness", value: 253 },
  { text:"SetObservationMode", value: 254 },
  { text:"SetObservationModeState", value: 255 },
  { text:"SetPDDIRGain", value: 256 },
  { text:"SetPDDIRShutterSpeed", value: 257 },
  { text:"SetBrightnessMode", value: 258 },
  { text:"SetPreFreezeLevel", value: 259 },
  { text:"SetDisplayStatus", value: 260 },
  { text:"SetElecZoom", value: 261 },
  { text:"SetImageSizeAsync", value: 262 },
  { text:"SetAgc", value: 263 },
  { text:"SetAgcMaxGain", value: 264 },
  { text:"SetOrientation", value: 265 },
  { text:"SetNBIColorMode", value: 266 },
  { text:"SetWLIColorMode", value: 267 },
  { text:"SetEightAxisTone", value: 268 },
  { text:"SetContrastLevel", value: 269 },
  { text:"SetNoiseReductionLevel", value: 270 },
  { text:"SetColorTone", value: 271 },
  { text:"SetIris", value: 272 },
  { text:"SetAutoIris", value: 273 },
  { text:"SetIrisArea", value: 274 },
  { text:"SetLightControlSpeed", value: 275 },
  { text:"GetIMMaskSize", value: 276 },
  { text:"VideoInputDetect", value: 277 },
  { text:"SetElecShutter", value: 278 },
  { text:"GetWbAverage", value: 279 },
  { text:"SetWbFactor", value: 280 },
  { text:"GetWbFactor", value: 281 },
  { text:"SetKindClvModel", value: 282 },
  { text:"SetDVISignalOutput", value: 283 },
  { text:"SetDisplayPortSignalOutput", value: 284 },
  { text:"SetSdiSignalOutput", value: 285 },
  { text:"GetImgSignal", value: 286 },
  { text:"SetTPBrightness", value: 287 },
  { text:"Set3DImgOutput", value: 288 },
  { text:"SetReplace", value: 289 },
  { text:"SetDepth", value: 290 },
  { text:"SetEndMask", value: 291 },
  { text:"SetFacingObservation", value: 292 },
  { text:"SetOsdOnoff", value: 293 },
  { text:"SetIconKind", value: 294 },
  { text:"SetModeIcon", value: 295 },
  { text:"SetFacingIcon", value: 296 },
  { text:"3DCoreAdjust", value: 297 },
  { text:"3DTestOutput", value: 298 },
  { text:"MemoryCheck", value: 299 },
  { text:"SetIRIColorMode", value: 300 },
  { text:"SetLaserLightControl", value: 301 },
  { text:"ScratchThrough", value: 302 },
  { text:"IF3DLRSelect", value: 303 },
  { text:"Set3DCoreAdjustValue", value: 304 },
  { text:"SetAspectAsync", value: 305 },
  { text:"SetIFRegSel", value: 306 },
  { text:"StartManualCoreAdjust", value: 307 },
  { text:"SetBladderColorCorrection", value: 308 },
  { text:"FreezeImageSelect", value: 309 },
  { text:"SetNoiseReductionParam", value: 310 },
  { text:"PIPPOP_INPUTSELECT", value: 311 },
  { text:"PIP_SET_SUB_DISP_POS", value: 312 },
  { text:"PIP_SET_SUB_DISP_SIZE", value: 313 },
  { text:"PIP_SET_MODE", value: 314 },
  { text:"POP_SET_MODE", value: 315 },
  { text:"PIPPOP_SELECT", value: 316 },
  { text:"SetMultiAxisTone", value: 317 },
  { text:"GetIHbAverage", value: 318 },
  { text:"SetColorEnhance", value: 319 },
  { text:"SetCbTargetFrame", value: 320 },
  { text:"SetColorMode", value: 321 },
  { text:"SetEDOF", value: 322 },
  { text:"SetImageSizeAsync2", value: 323 },
  { text:"SetIHbAverageCalcArea", value: 324 },
  { text:"SetIHbAverageDataRange", value: 325 },
  { text:"SetFrameRate", value: 326 },
  { text:"GetAgcGain", value: 327 },
  { text:"CalcCbFactor", value: 328 },
  { text:"GetCbFactor", value: 329 },
  { text:"SetCbFactor", value: 330 },
  { text:"GetCbAverage", value: 331 },
  { text:"SetCbScopeInfo", value: 332 },
  { text:"GetCbScopeInfo", value: 333 },
  { text:"SetCbCorrect", value: 334 },
  { text:"CalcCbLess", value: 335 },
  { text:"SetTransIllumination", value: 336 },
  { text:"SetTei", value: 337 },
  { text:"SetTeiMode", value: 338 },
  { text:"SetBaiMac", value: 339 },
  { text:"SetBaiMacLevel", value: 340 },
  { text:"SetMono", value: 341 },
  { text:"SetColorShiftCorrect", value: 342 },
  { text:"SetScpGain", value: 343 },
  { text:"SetIrisZoomArea", value: 344 },
  { text:"SetBloodVesselEnhLevel", value: 345 },
  { text:"SetDDIModeConfNumber", value: 346 },
  { text:"SetExtCvInput", value: 347 },
  { text:"SetExtCvMaskSizeParam", value: 348 },
  { text:"SetExtCvMessageParam", value: 349 },
  { text:"SetColorSpace", value: 350 },
  { text:"CheckEmoveCorrectStatus", value: 351 },
  { text:"SetEmoveFrontViewZoom", value: 352 },
  { text:"SetEmoveOnOff", value: 353 },
  { text:"SetEmoveIrisZoomArea", value: 354 },
  { text:"SetCbBaseFactor", value: 355 },
  { text:"SetLightCorrectParam", value: 356 },
  { text:"SetScopeColorTone", value: 357 },
  { text:"SetTdOutput", value: 358 },
  { text:"SetOutputImageKind", value: 359 },
  { text:"SetEDOFCorrectImageMode", value: 360 },
  { text:"SetLightSourceSpectrum", value: 361 },
  { text:"SetMovieOsdOnOff", value: 362 },
  { text:"SetFreezePreProc", value: 363 },
  { text:"SetDisplayFreeze", value: 364 },
  { text:"SetDisplayPortNoSync", value: 365 },
  { text:"SetHDR", value: 366 },
  { text:"GetRawInfo", value: 367 },
  { text:"SetOsdLayer", value: 368 },
  { text:"SetColorSpaceWithTerminal", value: 369 },
  { text:"GET", value: 370 },
  { text:"GET_UPDATE", value: 371 },
  { text:"GET_CALIB", value: 372 },
  { text:"SET", value: 373 },
  { text:"SET_UPDATE", value: 374 },
  { text:"SET_CALIB", value: 375 },
  { text:"CHECK", value: 376 },
  { text:"GET_VERSION", value: 377 },
  { text:"SET_CALIB_ANYDATA", value: 378 },
  { text:"GET_UNIT", value: 379 },
  { text:"GET_PACKAGE", value: 380 },
  { text:"SET_PACKAGE", value: 381 },
  { text:"GET_CALIB_ANYDATA", value: 382 },
  { text:"GET_ANYDATA", value: 383 },
  { text:"SET_ANYDATA", value: 384 },
  { text:"GET_SITARA_BOOT_STATUS", value: 385 },
  { text:"SET", value: 386 },
  { text:"REC", value: 387 },
  { text:"RELEASE", value: 388 },
  { text:"CAPTURE", value: 389 },
  { text:"CO2_SUPPLY", value: 390 },
  { text:"WATER_SUPPLY", value: 391 },
  { text:"TIP_HIGH", value: 392 },
  { text:"TIP_LOW", value: 393 },
  { text:"RING_HIGH", value: 394 },
  { text:"RING_LOW", value: 395 },
  { text:"WriteLog", value: 396 },
  { text:"Clear", value: 397 },
  { text:"Flush", value: 398 },
  { text:"TransferPause", value: 399 },
  { text:"TransferRestart", value: 400 },
  { text:"WritePause", value: 401 },
  { text:"WriteRestart", value: 402 },
  { text:"Flush_Strictly", value: 403 },
  { text:"ReadRegSpace", value: 404 },
  { text:"WriteRegSpace", value: 405 },
  { text:"CheckMemoryState", value: 406 },
  { text:"CHECK_INTERNAL_MEM_ENC_KEY", value: 407 },
  { text:"CREATE_INTERNAL_MEM_ENC_KEY", value: 408 },
  { text:"CREATE_IV", value: 409 },
  { text:"CREATE_EXTERNAL_MEM_ENC_PW", value: 410 },
  { text:"DELETE_EXTERNAL_MEM_ENC_PW", value: 411 },
  { text:"UPDATE_PREPARE", value: 412 },
  { text:"UPDATE_PREPARE_SP", value: 413 },
  { text:"UPDATE_START", value: 414 },
  { text:"UPDATE_EXEC", value: 415 },
  { text:"UPDATE_END", value: 416 },
  { text:"UPDATE_INFO", value: 417 },
  { text:"UPDATE_CANCEL", value: 418 },
  { text:"UPDATE_RECONFIG", value: 419 },
  { text:"INSP_JTAGCHECK", value: 420 },
  { text:"ROM_EXPORT", value: 421 },
  { text:"ROM_GETCRC", value: 422 },
  { text:"ECHO", value: 423 },
  { text:"MWM", value: 424 },
  { text:"CANCEL_MWM", value: 425 },
  { text:"MPPS_START", value: 426 },
  { text:"MPPS_END", value: 427 },
  { text:"PIC_STORE", value: 428 },
  { text:"CANCEL_PIC_STORE", value: 429 },
  { text:"PIC_STORECOMMIT", value: 430 },
  { text:"CANCEL", value: 431 },
  { text:"SECPOLICY_SET", value: 432 },
  { text:"SECPOLICY_DELETE", value: 433 },
  { text:"MAX", value: 434 },
  { text:"NWSET", value: 435 },
  { text:"MACADDRSET", value: 436 },
  { text:"MACADDRGET", value: 437 },
  { text:"MAX", value: 438 },
  { text:"SET_COM_PARAM", value: 439 },
  { text:"SESSION_DISCONNECT", value: 440 },
  { text:"INFO_CV_NET_CONNECTION", value: 441 },
  { text:"INFO_CV_PATIENT_INFORMATION_UPDATE", value: 442 },
  { text:"INFO_CV_PATIENT_INFORMATION_CANCEL", value: 443 },
  { text:"INFO_CV_EXAM_SELECT", value: 444 },
  { text:"INFO_CV_EXAM_START", value: 445 },
  { text:"INFO_CV_EXAM_END", value: 446 },
  { text:"INFO_CV_SCOPE_CONNECTION", value: 447 },
  { text:"INFO_CV_SCOPE_DISCONNECTION", value: 448 },
  { text:"INFO_CV_STOPWATCH_PUSH", value: 449 },
  { text:"INFO_CV_IS_EXAM_END_SETTING_CHANGE", value: 450 },
  { text:"INFO_CV_SCOPE_CHANGE", value: 451 },
  { text:"NET_SEND_PROCEDURE_INFORMATION_RESP", value: 452 },
  { text:"NET_SEND_FX_MESSAGE_RESP", value: 453 },
  { text:"NET_IMAGE_COUNT_REFFER_RESP", value: 454 },
  { text:"NET_PATIENT_QUERY", value: 455 },
  { text:"INFO_CV_EQUIPMENT_CONNECTION", value: 456 },
  { text:"INFO_CV_TRANSFER_IMAGE", value: 457 },
  { text:"EXAM_END_RESP", value: 458 },
  { text:"INFO_CV_NET_MILESTONE", value: 459 },
  { text:"PATIENT_COMMENT_RESP", value: 460 },
  { text:"MAX", value: 461 },
  { text:"SNTP", value: 462 },
  { text:"NTP", value: 463 },
  { text:"PING", value: 464 },
  { text:"TRACEROUTE", value: 465 },
  { text:"OCP_INITIALIZE", value: 466 },
  { text:"OCP_OPEN", value: 467 },
  { text:"TC_SETTING", value: 468 },
  { text:"START_COMMUNICATION", value: 469 },
  { text:"ETC_SETTING", value: 470 },
  { text:"ETC_START_COMM", value: 471 },
  { text:"ETC_STOP_COMM", value: 472 },
  { text:"CTRL_TRAFFIC", value: 473 },
  { text:"ETC_TLS_SETTING", value: 474 },
  { text:"EXECUTE_START", value: 475 },
  { text:"EXECUTE_END", value: 476 },
  { text:"STATE_NOTIFY", value: 477 },
  { text:"INSTRUCT", value: 478 },
  { text:"ID_DATA_READ", value: 479 },
  { text:"ID_DATA_WRITE", value: 480 },
  { text:"START_COUNTUP_DURATION", value: 481 },
  { text:"START_OWI_MONITORING", value: 482 },
  { text:"START_OMSC_MONITORING", value: 483 },
  { text:"START_HT_MONITORING", value: 484 },
  { text:"START_SCPSTS_MONITORING", value: 485 },
  { text:"GET_REGERROR1", value: 486 },
  { text:"SET_SUMCHECK", value: 487 },
  { text:"START_FOCUS_COPRO_SETUP", value: 488 },
  { text:"START_FOCUS_ACT_SETUP", value: 489 },
  { text:"START_FOCUS_AUTO_CALIBRATION", value: 490 },
  { text:"START_FOCUS_MANUAL_CALIBRATION", value: 491 },
  { text:"SET_FOCUS_CONTROL_MODE", value: 492 },
  { text:"START_FOCUS_MOVE", value: 493 },
  { text:"GET_FOCUS_MOVE_TIME", value: 494 },
  { text:"SET_LTA_HYSTERESIS", value: 495 },
  { text:"SET_FOCUS_TEST_MODE", value: 496 },
  { text:"SET_LTA_CURRENT", value: 497 },
  { text:"REMOVE_SCOPE", value: 498 },
  { text:"CVTYPE_SETTING", value: 499 },
  { text:"GET_SCP_SYSTEM_TYPE", value: 500 },
  { text:"SET_FOCUSMODE", value: 501 },
  { text:"SET_FOCUSSENSITIVITY", value: 502 },
  { text:"DRIVEFOCUS", value: 503 },
  { text:"INSP_DSP_RSEL", value: 504 },
  { text:"INSP_READ_SCPDATA", value: 505 },
  { text:"INSP_WRITE_SCPDATA", value: 506 },
  { text:"INSP_READ_SCPFLASHDATA", value: 507 },
  { text:"INSP_WRITE_SCPFLASHDATA", value: 508 },
  { text:"INSP_SET_SCPJIGMODE", value: 509 },
  { text:"INSP_READ_SCPDATA_ADDR32", value: 510 },
  { text:"INSP_WRITE_SCPDATA_ADDR32", value: 511 },
  { text:"ON", value: 512 },
  { text:"OFF", value: 513 },
  { text:"SET_VOLUME", value: 514 },
  { text:"SET_TIME", value: 515 },
  { text:"SET_TIME_ERA", value: 516 },
  { text:"GET_TIME", value: 517 },
  { text:"GET_TIME_ERA", value: 518 },
  { text:"INIT_TIME", value: 519 },
  { text:"GET_BATTERY_LEVEL", value: 520 },
  { text:"TO_JP_CALENDAR", value: 521 },
  { text:"TO_AD_CALENDAR", value: 522 },
  { text:"CALC_AGE", value: 523 },
  { text:"CALC_AGE_ERA", value: 524 },
  { text:"STOPWATCH", value: 525 },
  { text:"GET_STOPWATCH_CNT", value: 526 },
  { text:"GET_STOPWATCH_CNT_ERA", value: 527 },
  { text:"SET_DST_PARAMETER", value: 528 },
  { text:"SET_DST_STATE", value: 529 },
  { text:"DST_CONTROL", value: 530 },
  { text:"DST_CONVERT", value: 531 },
  { text:"GET_DATETIME_ALL", value: 532 },
  { text:"SET_ADJUST_TRIM", value: 533 },
  { text:"SET_STOPWATCH_CNT", value: 534 },
  { text:"DISP_LED", value: 535 },
  { text:"LedOff", value: 536 },
  { text:"LedOn", value: 537 },
  { text:"LedBlink", value: 538 },
  { text:"LedSetAutoMode", value: 539 },
  { text:"LedSetManualMode", value: 540 },
  { text:"GET_FSW_STATUS", value: 541 },
  { text:"GET_FPN_STATUS", value: 542 },
  { text:"MASK(exec_req)", value: 543 },
]