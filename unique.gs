function unique() {
  var filename = SpreadsheetApp.getActiveSheet().getName();
  var lastRow = SpreadsheetApp.getActiveSheet().getLastRow();
  var range = SpreadsheetApp.getActiveSheet().getRange(1, 1, lastRow, 4);
  var values = range.getValues();

  var duplicates = [];

  for (var i = 0; i < values.length - 1; i++) {
    if (values[i][0] === values[i+1][0] && values[i][1] === values[i+1][1]) {
      duplicates.push(i+1);
    }
  }

  for (var j = duplicates.length - 1; j >= 0; j--) {
    SpreadsheetApp.getActiveSheet().deleteRow(duplicates[j]);
  }
}
