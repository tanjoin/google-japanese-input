function export() {
  var CONTENT_TYPE = 'text/plain';
  var CHARSET = 'utf-8';
  var SEPARATOR = '\t';
  var NEWLINE = '\n';

  var filename = SpreadsheetApp.getActiveSheet().getName();
  var lastRow = SpreadsheetApp.getActiveSheet().getLastRow();
  var range = SpreadsheetApp.getActiveSheet().getRange(1, 1, lastRow, 4);
  var values = range.getValues();

  var dicList = [];
  for (i = 0; i < values.length; i++) {
    dicList.push(values[i].join(SEPARATOR));
  }
  var string = dicList.join(NEWLINE);

  filename = filename + '.txt';

  var blob = Utilities.newBlob("", CONTENT_TYPE, filename).setDataFromString(string, CHARSET);
  DriveApp.createFile(blob);
}

function exportWithName() {
  var CONTENT_TYPE = 'text/plain';
  var CHARSET = 'utf-8';
  var SEPARATOR = '\t';
  var NEWLINE = '\n';

  var lastRow = SpreadsheetApp.getActiveSheet().getLastRow();
  var range = SpreadsheetApp.getActiveSheet().getRange(1, 1, lastRow, 4);
  var values = range.getValues();

  var dicList = [];
  for (i = 0; i < values.length; i++) {
    dicList.push(values[i].join(SEPARATOR));
  }
  var string = dicList.join(NEWLINE);

  var filename = Browser.inputBox('保存名');

  filename = filename + '.txt';

  var blob = Utilities.newBlob("", CONTENT_TYPE, filename).setDataFromString(string, CHARSET);
  DriveApp.createFile(blob);
}
