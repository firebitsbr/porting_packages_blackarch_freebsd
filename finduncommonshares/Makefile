PORTNAME=	finduncommonshares
DISTVERSION=	3.2.r11.ga1f94dd
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python script allowing to quickly find uncommon shares in vast Windows Domains.
WWW=		https://github.com/p0dalirius/pyFindUncommonShares

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/impacket \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-sectools@${PY_FLAVOR} \
		??/py-xlsxwriter@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
