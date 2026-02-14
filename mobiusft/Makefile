PORTNAME=	mobiusft
DISTVERSION=	1.12
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An open-source forensic framework written in Python/GTK that manages cases and case items, providing an abstract interface for developing extensions.
WWW=		http://savannah.nongnu.org/projects/mobiusft

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	lang/python3

RUN_DEPENDS=	??/py-cairo@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/pygtk \
		??/sleuthkit \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
