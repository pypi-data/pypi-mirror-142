{{GOLANG_HEADER}}

package {{GOLANG_PACKAGE}}

import "github.com/kataras/iris/v12"

type RouteRegistrar func(router iris.Party)

var RouteRegistrars []RouteRegistrar

func AddRouteRegistrar(rr RouteRegistrar) {
	RouteRegistrars = append(RouteRegistrars, rr)
}

func RegisterRoutes(app iris.Party) {
	router := app.Group(conf.BasePath())

	for _, rr := range RouteRegistrars {
		rr(router)
	}
}
