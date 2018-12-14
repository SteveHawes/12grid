{
	"name": "flexitem",
	"displayName": "Flex Item",
	"version": 1,
	"definition": "flexitem/flexitem.json",
	"excludes": [
        "container",
        "column"
    ],
    "categoryName": "Flex CSS",
    "topContainer": true,
    "designStyleClass" : "customDivDesign",
	"model": {
		"class" :{ "type" :"styleclass", "tags": { "scope" :"design" }},
		"data-shrink" : {"type" :"string", "tags": { "scope" :"design" }, "values": ["0","1"], "default": "0"},
		"data-grow" : {"type" :"string", "tags": { "scope" :"design" }, "values": ["0","1"], "default": "0"},
		"data-align-self" : {"type" :"string", "tags": { "scope" :"design" }, "values": ["none", "center", "stretch", "baseline", "flex-start", "flex-end"], "default": "none"}
	}
}