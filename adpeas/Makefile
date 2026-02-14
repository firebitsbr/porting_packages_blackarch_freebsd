PORTNAME=	adpeas
DISTVERSION=	1.3.0.r15.g0bfcedc
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	winPEAS, but for Active Directory.
WWW=		https://github.com/ajm4n/adpeas

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/bloodhound \
		??/certi \
		??/certipy \
		??/impacket \
		??/netexec \
		??/py-ldap3@${PY_FLAVOR} \
		??/py-regex@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
