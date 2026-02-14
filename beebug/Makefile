PORTNAME=	beebug
DISTVERSION=	25.cddb375
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool for checking exploitability.
WWW=		https://github.com/invictus1306/beebug

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-pydot@${PY_FLAVOR} \
		??/py-pygraphviz@${PY_FLAVOR} \
		??/py-pyqtgraph@${PY_FLAVOR} \
		??/py-r2pipe@${PY_FLAVOR} \
		??/radare2 \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
