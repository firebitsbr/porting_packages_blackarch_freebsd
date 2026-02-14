PORTNAME=	networkmap
DISTVERSION=	58.f5faf17
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Post-exploitation network mapper.
WWW=		https://github.com/lorenzog/NetworkMap

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-decorator@${PY_FLAVOR} \
		??/py-ipaddress@${PY_FLAVOR} \
		??/py-networkx@${PY_FLAVOR} \
		??/py-nose@${PY_FLAVOR} \
		??/py-pydotplus@${PY_FLAVOR} \
		??/py-pyparsing@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
