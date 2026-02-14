PORTNAME=	ldapconsole
DISTVERSION=	2.1.0.r4.gc28c580
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Script allows you to perform custom LDAP requests to a Windows domain.
WWW=		https://github.com/p0dalirius/ldapconsole

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-ldap3@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-sectools@${PY_FLAVOR} \
		??/py-xlsxwriter@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
