{
	"name": "container",
	"displayName": "Container",
	"version": 1,
	"icon": "12grid/container.gif",
	"designStyleClass" : "rowDesign",
	"definition": "container.json",
	"contains": ["12grid.row","12grid.1column","12grid.2columns","12grid.3columns"],
	"topContainer": true,
	"model": {
		"class" :{ "type" :"styleclass", "tags": { "scope" :"design" } , "values" :["container","container-fluid"]}
	}
}