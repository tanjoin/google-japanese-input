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
    },
    {
      name: 'ユニーク化',
      functionName: 'unique'
    }
  ];
  spreadSheet.addMenu('辞書', subMenus);
}
