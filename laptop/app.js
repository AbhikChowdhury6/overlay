var RecordRTC = require('recordrtc');

var options = {
    recorderType: MediaStreamRecorder,
    mimeType: 'video/webm\;codecs=h264'
};
var recordRTC = RecordRTC(stream, options);
