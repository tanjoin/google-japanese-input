function onOpen() {
  var spreadSheet = SpreadsheetApp.getActiveSpreadsheet();
  var subMenus = [
    {
      name: 'エクスポート',
      functionName: 'export'
    },
    {
      name: '名前をつけてエクスポート',
      functionName: 'exportWithName'
    }
  ];
  spreadSheet.addMenu('辞書', subMenus);
}
