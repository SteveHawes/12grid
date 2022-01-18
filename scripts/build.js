var AdmZip = require('adm-zip');

// creating archives
var zip = new AdmZip();

zip.addLocalFolder("./META-INF/", "/META-INF/");
zip.addLocalFolder("./dist/12grid/", "/dist/12grid/");

zip.addLocalFolder("./lib/", "/lib/");

zip.addLocalFolder("./labelfield/", "/labelfield/");
zip.addLocalFolder("./2columns/", "/2columns/");
zip.addLocalFolder("./collapsible/", "/collapsible/");
zip.addLocalFolder("./container/", "/container/");
zip.addLocalFolder("./csspositioncontainer/", "/csspositioncontainer/");
zip.addLocalFolder("./div/", "/div/");
zip.addLocalFolder("./row/", "/row/");
zip.addLocalFolder("./responsivetable/", "/responsivetable/");
zip.addLocalFolder("./responsive_form/", "/responsive_form/");
zip.addLocalFolder("./simplecollapsible/", "/simplecollapsible/");
zip.addLocalFolder("./1column/", "/1column/");
zip.addLocalFolder("./clearfix/", "/clearfix/");
zip.addLocalFolder("./inlinegroup/", "/inlinegroup/");
zip.addLocalFolder("./flexlayout/", "/flexlayout/");
zip.addLocalFolder("./centercontainer/", "/centercontainer/");
zip.addLocalFolder("./flexitem/", "/flexitem/");
zip.addLocalFolder("./3columns/", "/3columns/");
zip.addLocalFolder("./2screens/", "/2screens/");
zip.addLocalFolder("./flexcontainer/", "/flexcontainer/");
zip.addLocalFolder("./column/", "/column/");

zip.writeZip("12grid.zip")