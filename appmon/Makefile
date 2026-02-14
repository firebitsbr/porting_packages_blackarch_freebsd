PORTNAME=	appmon
DISTVERSION=	0.5.r36.gf753c4d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A runtime security testing & profiling framework for native apps on macOS, iOS & android and it is built using Frida.
WWW=		https://github.com/dpnishant/appmon

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-alembic@${PY_FLAVOR} \
		??/py-banal@${PY_FLAVOR} \
		??/py-chardet@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-dataset@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-editor@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-frida@${PY_FLAVOR} \
		??/py-htmlentities@${PY_FLAVOR} \
		??/py-itsdangerous@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-mako@${PY_FLAVOR} \
		??/py-markupsafe@${PY_FLAVOR} \
		??/py-normality@${PY_FLAVOR} \
		??/py-sqlalchemy@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-werkzeug@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
