PORTNAME=	ad-ldap-enum
DISTVERSION=	88.60bc5bb
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An LDAP based Active Directory user and group enumeration tool.
WWW=		https://github.com/CroweCybersecurity/ad-ldap-enum

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/dos2unix \
		devel/git

RUN_DEPENDS=	??/py-ldap3@${PY_FLAVOR} \
		??/py-openpyxl@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
