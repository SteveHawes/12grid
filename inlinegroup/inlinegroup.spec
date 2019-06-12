{
    "name": "inlinegroup",
    "displayName": "Inline Group Container",
    "version": 1,
    "icon": "12grid/inlinegroup/inlinegroup.png",
    "definition": "inlinegroup/inlinegroup.json",
    "excludes": [
        "container",
        "column",
        "flexitem"
    ],
    "designStyleClass" : "inlinegroupDesign",
    "categoryName": "Templates",
    "topContainer": true,
     "model": {
		"class" :{ "type" :"styleclass", "tags": { "scope" :"design" }},
		"data-leftsize" : {"type" :"string", "tags": { "scope" :"design" }, "values": ["auto","xs", "sm", "md", "lg"], "default": "auto"},
		"data-rightsize" : {"type" :"string", "tags": { "scope" :"design" }, "values": ["auto","xs", "sm", "md", "lg"], "default": "auto"},
		"data-responsive" : {"type" :"string", "tags": { "scope" :"design" }, "values": ["none", "col-sm", "col-md", "col-lg"], "default": "none"}
	}
}