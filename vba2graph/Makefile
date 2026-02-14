PORTNAME=	vba2graph
DISTVERSION=	29.fcf96ef
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Generate call graphs from VBA code, for easier analysis of malicious documents.
WWW=		https://github.com/MalwareCantFly/Vba2Graph

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/graphviz \
		??/py-graphviz@${PY_FLAVOR} \
		??/py-networkx@${PY_FLAVOR} \
		??/py-pydot@${PY_FLAVOR} \
		??/py-regex@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
