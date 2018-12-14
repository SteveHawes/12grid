{
	"name": "flexcontainer",
	"displayName": "Flex Container",
	"version": 1,
	"definition": "flexcontainer/flexcontainer.json",
    "excludes": [
        "container",
        "column"
    ],
    "categoryName": "Flex CSS",
    "topContainer": true,
    "designStyleClass" : "customDivDesign",
	"model": {
		"class" :{ "type" :"styleclass", "tags": { "scope" :"design" }},
		"data-direction" : {"type" :"string", "tags": { "scope" :"design" }, "values": ["row","column"], "default": "row"},
		"data-justify-content" : {"type" :"string", "tags": { "scope" :"design" }, "values": ["center", "space-between", "space-around", "space-evenly", "flex-start", "flex-end"], "default": "flex-start"},
		"data-align-items" : {"type" :"string", "tags": { "scope" :"design" }, "values": ["center", "stretch", "baseline", "flex-start", "flex-end"], "default": "stretch"}
	}
}