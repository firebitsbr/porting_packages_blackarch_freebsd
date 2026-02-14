PORTNAME=	hate-crack
DISTVERSION=	367.1fab01d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool for automating cracking methodologies through Hashcat.
WWW=		https://github.com/trustedsec/hate_crack

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/hashcat \
		??/py-pyenchant@${PY_FLAVOR} \
		??/pygtk \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
