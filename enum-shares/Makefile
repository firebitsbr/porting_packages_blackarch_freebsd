PORTNAME=	enum-shares
DISTVERSION=	7.97cba5a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tool that enumerates shared folders across the network and under a custom user account.
WWW=		https://github.com/dejanlevaja/enum_shares

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-ipcalc@${PY_FLAVOR} \
		??/py-pysmb@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
