{
	"name": "column",
	"displayName": "Column",
	"version": 1,
	"icon": "12grid/column.png",
	"designStyleClass" : "columnDesign",
	"definition": "column.json",
	"excludes": ["container","column","flexitem"],
	"model": {
		"class" :{ "type" :"styleclass", "tags": { "scope" :"design" } , "values" :["col-xs-","col-sm-","col-md-","col-md-4","col-lg-","col-xs-offset-","col-sm-offset-","col-md-offset-","col-lg-offset-"]}
	}
}
